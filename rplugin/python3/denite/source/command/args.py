from denite.source.command import Source as Command, Kind as CommandKind


class Source(Command):
    def __init__(self, vim) -> None:
        super().__init__(vim)

        self.name = 'command/args'
        self.kind = Kind(vim)
        self._saved_compl = {}

    def _get_command_completion(self, prefix):
        cpl = []
        if prefix in self._saved_compl:
            cpl = self._saved_compl[prefix]
        else:
            cpl = self.vim.call('denite_command_args#getcmdcompletion', prefix)
            self._saved_compl[prefix] = cpl
        return [''] + cpl

    def gather_candidates(self, context):
        context['is_interactive'] = True
        args = ' '.join(context['args'])
        if args:
            args += ' '

        has_cmdline = self.vim.call('denite#helper#has_cmdline')
        if not has_cmdline:
            return []
        return [{
            'action__command': args + x,
            'word': args + x,
            'action__histadd': True,
        } for x in self._get_command_completion(args)]


class KindMixin():
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'command/args'

    def action_narrow(self, context):
        context['sources_queue'].append([{
            'name': 'command/args',
            'args': '  '.join(x['action__command'].split(':')).split(' ')
        } for x in context['targets']])

    def action_args(self, context):
        return self.action_narrow(context)

    def action_edit(self, context):
        target = context['targets'][0]
        self.vim.call('feedkeys', f":{target['action__command']}")


class Kind(KindMixin, CommandKind):
    pass

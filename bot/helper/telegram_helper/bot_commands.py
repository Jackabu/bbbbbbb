from bot import CMD_INDEX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_COMMAND', f'start{CMD_INDEX}')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'mirror{CMD_INDEX}')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'unzipmirror{CMD_INDEX}')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'zipmirror{CMD_INDEX}')
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'cancel{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', f'cancelall{CMD_INDEX}')
        self.ListCommand = getCommand('LIST_COMMAND', f'list{CMD_INDEX}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'status{CMD_INDEX}')
        self.PingCommand = getCommand('PING_COMMAND', f'ping{CMD_INDEX}')
        self.RestartCommand =  getCommand('RESTART_COMMAND', f'restart{CMD_INDEX}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats{CMD_INDEX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'help{CMD_INDEX}')
        self.CloneCommand = getCommand('CLONE_COMMAND', f'clone{CMD_INDEX}')
        self.CountCommand = getCommand('COUNT_COMMAND', f'count{CMD_INDEX}')
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'watch{CMD_INDEX}')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'zipwatch{CMD_INDEX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'qbmirror{CMD_INDEX}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'qbunzipmirror{CMD_INDEX}')
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'qbzipmirror{CMD_INDEX}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del{CMD_INDEX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'leechset{CMD_INDEX}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'setthumb{CMD_INDEX}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'leech{CMD_INDEX}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'unzipleech{CMD_INDEX}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'zipleech{CMD_INDEX}')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'qbleech{CMD_INDEX}')
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'qbunzipleech{CMD_INDEX}')
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'qbzipleech{CMD_INDEX}')
        self.LeechWatchCommand =getCommand('LEECHWATCH_COMMAND',  f'leechwatch{CMD_INDEX}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'leechzipwatch{CMD_INDEX}')

BotCommands = _BotCommands()

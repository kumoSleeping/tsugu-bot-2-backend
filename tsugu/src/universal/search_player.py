from ...utils import text_response, User, server_id_2_server_name, server_name_2_server_id, server_exists, config
from tsugu_api_core._typing import _ServerName
import tsugu_api
from arclet.alconna import Alconna, Option, Subcommand, Args, CommandMeta, Empty, Namespace, namespace, command_manager


def handler(message: str, user: User, platform: str, channel_id: str):
    res = Alconna(
        ["查玩家", "查寻玩家"],
        Args["playerId#你的游戏账号(数字)", int]["serverName;?#省略服务器名时，默认从你当前的主服务器查询。", _ServerName.__args__],
        meta=CommandMeta(
            compact=config.compact, description="查询玩家信息",
            usage='查询指定ID玩家的信息。查询指定ID玩家的信息。',
            example='查玩家 40474621 jp : 查询日服玩家ID为40474621的玩家信息。\n查玩家 10000000 : 查询你当前默认服务器中，玩家ID为10000000的玩家信息。',
        )
    ).parse(message)

    if res.matched:
        if res.serverName:
            server = res.serverName
        else:
            server = user.server_mode
        return tsugu_api.search_player(res.playerId, server)

    return res



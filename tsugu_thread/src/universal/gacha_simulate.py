from ...utils import get_user, text_response, User, server_id_2_server_name, server_name_2_server_id
import tsugu_api
from arclet.alconna import Alconna, Option, Subcommand, Args, CommandMeta, Empty, Namespace, namespace, command_manager


alc = Alconna(
        ["抽卡模拟", "卡池模拟"],
        Args["times", int, 10]['gacha_id;?#如果没有卡池ID的话，卡池为当前活动的卡池。', int],
        meta=CommandMeta(
            compact=True, description="抽卡模拟",
            usage='根据卡片ID查询卡片插画',
            example='抽卡模拟 300 922 :模拟抽卡300次，卡池为922号卡池。'
        )
    )


def handler(message: str, user_id: str, platform: str, channel_id: str):
    res = alc.parse(message)

    if res.matched:
        user = get_user(user_id, platform)
        if res.gacha_id:
            gacha_id = res.gacha_id
        else:
            gacha_id = None
        return tsugu_api.gacha_simulate(user.server_mode, res.times, gacha_id)

    return res
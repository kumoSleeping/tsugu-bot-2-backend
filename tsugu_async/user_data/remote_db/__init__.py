
from ...utils import text_response, server_exists
import tsugu_api_async
import time
from ...utils import User
from ...utils import config
from aiologger import Logger

logger = Logger.with_default_handlers()


async def get_user(user_id: str, platform: str) -> User:
    for i in range(0, config.get_remote_user_data_max_retry):
        try:
            user_data_res = await tsugu_api_async.get_user_data(platform, user_id)
            if user_data_res.get('status') == 'failed':
                return text_response(user_data_res.get('data'))
            break
        except Exception as e:
            logger.error(f'Error: {e}')
            time.sleep(0.5)
            continue
    else:
        return text_response('网络链接异常')

    # 获取用户数据失败
    if user_data_res.get('status') == 'failed':
        return text_response(user_data_res.get('data'))
    # 构建用户对象
    user_data = user_data_res.get('data')
    user = User(user_id, platform, user_data['server_mode'], user_data['default_server'], user_data['car'], user_data['server_list'])# type: ignore
    return user
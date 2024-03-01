from tsugu import tsugu_config, tsugu_bot
import unittest


class TestTsugu(unittest.TestCase):

    def test_tsugu(self):
        def show_back_msg(data):
            import base64
            from PIL import Image
            import io

            if not data:
                return "[无反馈数据]"

            for item in data:
                if item["type"] == "string":
                    print(f"[文字信息]\n{item['string']}")
                elif item["type"] == "base64":
                    image_data = base64.b64decode(item["string"])
                    print(f"[图像大小: {len(image_data) / 1024:.2f}KB]")
                    Image.open(io.BytesIO(image_data)).show()
                else:
                    print(item)

        # self.subTest(
        #     tsugu_config.config_docs()
        # )
        tsugu_config.backend = 'http://127.0.0.1:3000'
        tsugu_config.utils_backend = 'http://127.0.0.1:3000'
        self.subTest(
            show_back_msg(
                tsugu_bot('查卡 ', '114514', 'red', '666808414'),
            )
        )


if __name__ == '__main__':
    unittest.main()



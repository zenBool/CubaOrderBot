import aiogram.types

from .consts import DefaultConstructor


class BasicButtons(DefaultConstructor):
    @staticmethod
    def back() -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["◀️ Back"]
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def cancel() -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["🚫 Cancel"]
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def back_n_cancel() -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1, 1]
        btns = ["◀️ Back", "🚫 Cancel"]
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def confirmation(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = []
        btns = []
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Cancel")
        schema.append(1)
        btns.append("✅ Ok")
        if add_back:
            schema.append(1)
            btns.append("◀️ Back")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def skip(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["▶️Пропустить"]
        if add_back:
            schema.append(1)
            btns.append("◀️ Back")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Cancel")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def yes(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["✅Да"]
        if add_back:
            schema.append(1)
            btns.append("◀️ Back")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Cancel")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def no(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [1]
        btns = ["❌Нет"]
        if add_back:
            schema.append(1)
            btns.append("◀️ Back")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Cancel")
        return BasicButtons._create_kb(btns, schema)

    @staticmethod
    def yes_n_no(
        add_back: bool = False, add_cancel: bool = False
    ) -> aiogram.types.ReplyKeyboardMarkup:
        schema = [2]
        btns = ["✅ Yes", "❌ No"]
        if add_back:
            schema.append(1)
            btns.append("◀️ Back")
        if add_cancel:
            schema.append(1)
            btns.append("🚫 Cancel")
        return BasicButtons._create_kb(btns, schema)

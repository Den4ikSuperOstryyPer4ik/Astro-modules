#
# 	 @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
# 	@@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
# 	@@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
# 	!@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
# 	@!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
# 	!!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
# 	!!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
# 	:!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
# 	::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
# 	 :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
#
#                                             © Copyright 2024
#
#                                    https://t.me/Den4ikSuperOstryyPer4ik
#                                                  and
#                                          https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/MineSwepper.png
# meta developer: @AstroModules

import random

from .. import loader, utils


class Cell:
    """Cell on the minesweeper board"""

    def __init__(self, value: int = 0, is_mine: bool = False, is_visible: bool = False):
        self.is_mine = is_mine
        self.value = value
        self.is_visible = is_visible
        self.emoji = "◽️"
        self.emoji2 = "ㅤ"


class MineSweeperGame:
    """Minesweeper game"""

    def __init__(self, rows: int, cols: int, mines: int):
        self.mode = 1  # 1 - miner, 2 - flag
        self.flags = 0
        self.board: list[list[Cell]] = []
        self.rows = rows
        self.cols = cols
        self.mines = mines

    def generate_board(self):
        """Generate the minesweeper board"""
        self.board = [
            [
                Cell()
                for _ in range(self.cols)
            ] for _ in range(self.rows)
        ]
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for position in mine_positions:
            row = position // self.cols
            col = position % self.cols
            self.board[row][col].value = None
            self.board[row][col].is_mine = True
            self.board[row][col].emoji2 = "💣"
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < self.rows and 0 <= j < self.cols and not self.board[i][j].is_mine:
                        self.board[i][j].value += 1

        for row in self.board:
            for cell in row:
                if cell.value:
                    cell.emoji2 = {
                        1: "1️⃣",
                        2: "2️⃣",
                        3: "3️⃣",
                        4: "4️⃣",
                        5: "5️⃣",
                        6: "6️⃣",
                        7: "7️⃣",
                        8: "8️⃣",
                    }[cell.value]

    def reveal_cell(self, row_index, col):
        """Reveal a cell on the minesweeper board"""
        if self.board[row_index][col].is_mine:
            if len([
                cell
                for row in self.board
                for cell in row
                if cell.is_visible
            ]) in [0, 1]:
                self.generate_board()
                return self.reveal_cell(row_index, col)
            return False
        elif self.board[row_index][col].value == 0:
            self._reveal_empty_cells(row_index, col)
        else:
            self.board[row_index][col].is_visible = True
        return self.board

    def reveal_next_to_empty_cells(self):
        """Reveal all next to empty cells"""
        for index_row, row in enumerate(self.board):
            for index_cell, cell in enumerate(row):
                if cell.value == 0 and cell.is_visible:
                    for i in range(index_row - 1, index_row + 2):
                        for j in range(index_cell - 1, index_cell + 2):
                            if 0 <= i < self.rows and 0 <= j < self.cols:
                                if not self.board[i][j].is_mine and not self.board[i][j].is_visible:
                                    self.reveal_cell(i, j)

    def _reveal_empty_cells(self, row, col):
        """Reveal all empty cells connected to the given cell"""
        if self.board[row][col].value == 0:
            self.board[row][col].is_visible = True
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < self.rows and 0 <= j < self.cols:
                        if not self.board[i][j].is_mine and not self.board[i][j].is_visible and self.board[i][j].value == 0:
                            self.reveal_cell(i, j)


class MineSwepperModule(loader.Module):
    """Minesweeper game"""

    strings = {
        "name": "MineSweeper",
        "mines": "Number of mines",
        "rows": "Number of rows",
        "cols": "Number of columns",
        "game": "🎮 <b>MineSweeper game</b>\n\n💣 <b>{mines}</b> mines\n🧮 <b>{rows}</b> rows\n💈 <b>{cols}</b> columns\n🚩 <b>{flags}</b> flags",
        "game-over": "❌ <b>Game over!</b>\n💣 <b>You hit a mine.</b>\n\n💣 <b>{mines}</b> mines\n🧮 <b>{rows}</b> rows\n💈 <b>{cols}</b> columns\n🚩 <b>{flags}</b> flags",
        "game-end": "❌ <b>Game over!</b>\n🎉 <b>You win!</b>\n\n💣 <b>{mines}</b> mines\n🧮 <b>{rows}</b> rows\n💈 <b>{cols}</b> columns\n🚩 <b>{flags}</b> flags",
        "game-ended": "❌ Game over!",
        "continue-or-start-new-game": "⚠️ <b>Game already started!</b>\n❔ Continue or start new game?",
        "continue": "▶️ Continue",
        "start-new-game": "🆕 Start new game",
        "game-title": "🎮 <b>MineSweeper game</b>",
        "game-not-found": "❌ Game not found!",
        "cell-flagged": "🚩 Cell flagged",
        "switch-mode": "🔄 Switch to «🚩» mode",
    }

    strings_ru = {
        "_cls_doc": "Игра \"Сапёр\"",
        "mines": "Количество мин",
        "rows": "Количество строк",
        "cols": "Количество столбцов",
        "game": "🎮 <b>Игра \"Сапёр\"</b>\n\n💣 <b>{mines}</b> мин\n🧮 <b>{rows}</b> строк\n💈 <b>{cols}</b> столбцов\n🚩 <b>{flags}</b> флагов",
        "game-over": "❌ <b>Игра окончена!</b>\n<b>💣 Вы попали на мину.</b>\n\n💣 <b>{mines}</b> мин\n🧮 <b>{rows}</b> строк\n💈 <b>{cols}</b> столбцов\n🚩 <b>{flags}</b> флагов",
        "game-end": "❌ <b>Игра окончена!</b> \n<b>🎉 Вы выиграли!</b>\n\n💣 <b>{mines}</b> мин\n🧮 <b>{rows}</b> строк\n💈 <b>{cols}</b> столбцов\n🚩 <b>{flags}</b> флагов",
        "game-ended": "❌ Игра окончена!",
        "continue-or-start-new-game": "⚠️ <b>В этом чате уже идёт игра!</b>\n❔ Продолжить или начать новую игру?",
        "continue": "▶️ Продолжить",
        "start-new-game": "🆕 Начать новую игру",
        "game-title": "🎮 <b>Игра \"Сапёр\"</b>",
        "game-not-found": "❌ Игра не найдена! Возможно она уже завершена.",
        "cell-flagged": "🚩 Поле помечено",
        "switch-mode": "🔄 Переключиться на режим «{}»"
    }

    def __init__(self):
        self.games = {}
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "mines",
                10,
                lambda: self.strings("mines"),
                validator=loader.validators.Integer(minimum=1, maximum=99),
            ),
            loader.ConfigValue(
                "rows",
                8,
                lambda: self.strings("rows"),
                validator=loader.validators.Integer(minimum=1, maximum=10),
            ),
            loader.ConfigValue(
                "cols",
                8,
                lambda: self.strings("cols"),
                validator=loader.validators.Integer(minimum=1, maximum=8),
            )
        )

    def generate_markup(self, chat_id):
        if not self.games.get(chat_id):
            return

        return [
            [
                {
                    "text": i.emoji2 if i.is_visible else i.emoji,
                    "callback": self.mine if self.games.get(chat_id).mode == 1 else self.flag,
                    "kwargs": {
                        "row": self.games.get(chat_id).board.index(row),
                        "col": row.index(i),
                        "chat_id": chat_id
                    }
                }
                for i in row
            ]
            for row in self.games.get(chat_id).board
        ] + [
            [
                {
                    "text": self.strings("switch-mode").format('🚩' if self.games.get(chat_id).mode == 1 else '⛏️'),
                    "callback": self.switch_mode,
                    "kwargs": {
                        "chat_id": chat_id
                    }
                }
            ]
        ]

    async def switch_mode(self, call, chat_id):
        self.games.get(chat_id).mode = 1 if self.games.get(chat_id).mode == 2 else 2
        await call.edit(
            self.strings("game").format(
                mines=self.games.get(chat_id).mines,
                rows=self.games.get(chat_id).rows,
                cols=self.games.get(chat_id).cols,
                flags=self.games.get(chat_id).flags
            ),
            reply_markup=self.generate_markup(chat_id)
        )

    async def flag(self, call, row, col, chat_id):
        if self.games.get(chat_id).mode != 2:
            return

        if self.games.get(chat_id).board[row][col].emoji != "🚩":
            self.games.get(chat_id).flags += 1
            self.games.get(chat_id).board[row][col].emoji = "🚩"
        else:
            self.games.get(chat_id).flags -= 1
            self.games.get(chat_id).board[row][col].emoji = "◽️"

        await call.edit(
            self.strings("game").format(
                mines=self.games.get(chat_id).mines,
                rows=self.games.get(chat_id).rows,
                cols=self.games.get(chat_id).cols,
                flags=self.games.get(chat_id).flags
            ),
            reply_markup=self.generate_markup(chat_id)
        )

    @loader.command(
        ru_doc="- начать игру \"Сапёр\"",
        alias="mines",
    )
    async def minesweeper(self, message):
        """- start the game "Minesweeper" """
        chat_id: int = utils.get_chat_id(message)
        if chat_id in self.games:
            await utils.answer(message, self.strings("continue-or-start-new-game"), reply_markup=[
                [
                    {
                        "text": self.strings("continue"),
                        "callback": self.continue_game,
                        "kwargs": {
                            "chat_id": chat_id
                        }
                    }
                ],
                [
                    {
                        "text": self.strings("start-new-game"),
                        "callback": self.start_game,
                        "kwargs": {
                            "chat_id": chat_id
                        }
                    }
                ]
            ])
        else:
            await utils.answer(message, self.strings("game-title"), reply_markup=[
                [
                    {
                        "text": self.strings("start-new-game"),
                        "callback": self.start_game,
                        "kwargs": {
                            "chat_id": chat_id
                        }
                    }
                ]
            ])

    async def start_game(self, call, chat_id: int):
        self.games[chat_id] = MineSweeperGame(
            rows=self.config["rows"],
            cols=self.config["cols"],
            mines=self.config["mines"],
        )
        self.games.get(chat_id).generate_board()
        await call.edit(
            self.strings("game").format(
                mines=self.games.get(chat_id).mines,
                rows=self.games.get(chat_id).rows,
                cols=self.games.get(chat_id).cols,
                flags=self.games.get(chat_id).flags
            ),
            reply_markup=self.generate_markup(chat_id)
        )

    async def continue_game(self, call, chat_id: int):
        await call.edit(
            self.strings("game").format(
                mines=self.games.get(chat_id).mines,
                rows=self.games.get(chat_id).rows,
                cols=self.games.get(chat_id).cols,
                flags=self.games.get(chat_id).flags
            ),
            reply_markup=self.generate_markup(chat_id)
        )

    async def mine(self, call, row, col, chat_id):
        if not self.games.get(chat_id, None):
            return await call.answer(self.strings("game-not-found"), show_alert=True)
        if self.games.get(chat_id).board[row][col].emoji == "🚩":
            return await call.answer(self.strings("cell-flagged"), show_alert=True)

        result = self.games.get(chat_id).reveal_cell(row, col)
        self.games.get(chat_id).reveal_next_to_empty_cells()

        if not result or len([
            i
            for row in self.games.get(chat_id).board
            for i in row
            if not i.is_visible
        ]) == self.games.get(chat_id).mines:
            await call.edit(
                self.strings("game-over" if not result else "game-end").format(
                    mines=self.games.get(chat_id).mines,
                    rows=self.games.get(chat_id).rows,
                    cols=self.games.get(chat_id).cols,
                    flags=self.games.get(chat_id).flags
                ),
                reply_markup=[
                    [
                        {
                            "text": i.emoji2,
                            "action": "answer",
                            "message": self.strings("game-ended")
                        }
                        for i in row
                    ]
                    for row in self.games.get(chat_id).board
                ] + [
                    [
                        {
                            "text": self.strings("start-new-game"),
                            "callback": self.start_game,
                            "kwargs": {
                                "chat_id": chat_id
                            }
                        }
                    ]
                ])
            del self.games[chat_id]
        else:
            await call.edit(
                self.strings("game").format(
                    mines=self.games.get(chat_id).mines,
                    rows=self.games.get(chat_id).rows,
                    cols=self.games.get(chat_id).cols,
                    flags=self.games.get(chat_id).flags
                ),
                reply_markup=self.generate_markup(chat_id)
            )

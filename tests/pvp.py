import unittest
from unittest.mock import patch

from t3.game import Game
from tests.core import BaseTest


class TwoPlayerGameTest(BaseTest):

    def test_player_1_winner(self):
        game = Game(False)

        @patch('builtins.input')
        def run(m_input):
            m_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            game.start()

        run()
        game.declare_winner()
        state = game.get_state()
        self.assertTrue(state.get('is_player_1_winner'))
        self.assertEqual(['❌', '⭕', '❌', '⭕', '❌', '⭕', '❌', '8️⃣', '9️⃣'], state.get('board'))

    def test_tie(self):
        game = Game(False)

        @patch('builtins.input')
        def run(m_input):
            m_input.side_effect = ['5', '1', '2', '8', '3', '7', '9', '6', '4']
            game.start()

        run()
        game.declare_winner()
        state = game.get_state()
        self.assertIsNone(state.get('is_player_1_winner'))
        self.assertEqual(['⭕', '❌', '❌', '❌', '❌', '⭕', '⭕', '⭕', '❌'], state.get('board'))


if __name__ == '__main__':
    unittest.main()

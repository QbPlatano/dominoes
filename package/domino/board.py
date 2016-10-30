import collections
import domino

class Board:
    '''
    Python class for objects that represent a domino board.
    A domino board consists of a series of dominoes placed
    end to end such that the values on connected ends match.

    Usage::
        >>> import domino
        >>> d1 = domino.Domino(1, 2)
        >>> d2 = domino.Domino(1, 3)
        >>> b = domino.Board()
        >>> b

        >>> b.add_left(d1)
        >>> b
        [1|2]
        >>> b.add_right(d2)
        EndsMismatchException: [1|3] cannot be added to the right of the board - values do not match!
        >>> b.add_left(d2)
        >>> b
        [3|1][1|2]
        >>> b.left_end()
        3
        >>> b.right_end()
        2
        >>> len(b)
        2
    '''
    def __init__(self):
        self.board = collections.deque()

    def left_end(self):
        '''
        Returns the outward-facing value on the left end of the
        board. Raises an EmptyBoardException if the board is empty.
        '''
        try:
            return self.board[0].first
        except IndexError:
            raise domino.EmptyBoardException('Cannot retrieve the left end of'
                                             ' the board because it is empty!')

    def right_end(self):
        '''
        Returns the outward-facing value on the right end of the
        board. Raises an EmptyBoardException if the board is empty.
        '''
        try:
            return self.board[-1].second
        except IndexError:
            raise domino.EmptyBoardException('Cannot retrieve the right end of'
                                             ' the board because it is empty!')

    def add_left(self, d):
        '''
        Adds the provided domino to the left end of the board.
        Raises an EndsMismatchException if the values do not match.

        :param Domino d: domino to add
        '''
        if not self:
            self.board.append(d)
        elif d.first == self.left_end():
            self.board.appendleft(d.inverted())
        elif d.second == self.left_end():
            self.board.appendleft(d)
        else:
            raise domino.EndsMismatchException(
                '{} cannot be added to the left of'
                ' the board - values do not match!'.format(d)
            )

    def add_right(self, d):
        '''
        Adds the provided domino to the right end of the board.
        Raises an EndsMismatchException if the values do not match.

        :param Domino d: domino to add
        '''
        if not self:
            self.board.append(d)
        elif d.first == self.right_end():
            self.board.append(d)
        elif d.second == self.right_end():
            self.board.append(d.inverted())
        else:
            raise domino.EndsMismatchException(
                '{} cannot be added to the right of'
                ' the board - values do not match!'.format(d)
            )

    def __len__(self):
        return len(self.board)

    def __str__(self):
        return ''.join(str(d) for d in self.board)

    def __repr__(self):
        return str(self)

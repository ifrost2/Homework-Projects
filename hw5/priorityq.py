import heapq
import itertools



############################################################
#********************PQ Class*****************************
############################################################
'''
An implementation of a priority queue that you can use with
your A* search.

https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes

NOTE: Do NOT edit
'''
class PQ:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    ############################################################
    '''
    Adds game with the specified priority to the q
    If game already exists, updates the game's priority.
    '''
    def update(self, game, priority=0):
        hash = game.hash()

        'Add a new task or update the priority of an existing task'
        if hash in self.entry_finder:
            self.remove_game(game)
        count = next(self.counter)
        entry = [priority, count, game]
        self.entry_finder[hash] = entry
        heapq.heappush(self.pq, entry)

    ############################################################


    ############################################################
    '''
    Removes the game from the q
    '''
    def remove_game(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task.hash())
        entry[-1] = self.REMOVED

    ############################################################

    ############################################################
    '''
    Removes the lowest priority game from the q
    '''
    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task.hash()]
                return task
        raise KeyError('pop from an empty priority queue')

    ############################################################

    ############################################################
    '''
    Returns true if the q is empty
    '''
    def isEmpty(self):
        for item in self.pq:
            if item is not self.REMOVED:
                return False
        return True
    ############################################################


    ############################################################
    '''
    Returns priority if the game is in the q,
    and returns -1 if the game is not
    '''
    def getPriority(self, game):
        hash = game.hash()
        if hash in self.entry_finder:
            return self.entry_finder[hash][0]
        else:
            return -1
    ############################################################


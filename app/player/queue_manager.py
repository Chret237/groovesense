from recommendation.recommender import (
    recommend_next_song
)

class QueueManager:

    def __init__(self):

        self.queue = []

    def add_song(self, song):

        self.queue.append(song)

    def get_next_song(self):

        return self.queue.pop(0)
    
    def preload_queue(session, library, queue_manager):
        while len(queue_manager.queue) < 3:

            recommendation = (
                recommend_next_song(
                    current_state={
                        "current_bpm":
                        session.current_bpm,

                        "current_energy":
                        session.current_energy,

                        "current_mood":
                        session.current_mood
                    },

                    library=library,

                    played_songs=
                    session.played_songs
                )
            )

            queue_manager.add_song(
                recommendation["song"]
            )
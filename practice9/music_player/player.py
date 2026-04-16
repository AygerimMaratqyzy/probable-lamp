import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.index = 0

        self.is_playing = False
        self.paused = False

        pygame.mixer.init()

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))
        files.sort()
        return files

    #PLAY / RESUME
    def play(self):
        if not self.playlist:
            return

        # If paused,then resume
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.is_playing = True
            return

        # Start new playback
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()
        self.is_playing = True

    #PAUSE
    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True
        self.is_playing = False

    #STOP (fully reset)
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.paused = False

    #NEXT TRACK
    def next(self):
        if not self.playlist:
            return
        self.index = (self.index + 1) % len(self.playlist)
        self.paused = False
        self.play()

    #PREVIOUS TRACK
    def previous(self):
        if not self.playlist:
            return
        self.index = (self.index - 1) % len(self.playlist)
        self.paused = False
        self.play()

    #CURRENT TRACK NAME
    def get_current_track(self):
        if not self.playlist:
            return "No music found"
        return os.path.basename(self.playlist[self.index])
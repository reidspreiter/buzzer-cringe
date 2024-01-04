from picozero import RGBLED, Speaker

rgb  = RGBLED(red=13, green=14, blue=15)
speaker = Speaker(12)

moog_city = [330, 440, 494, 659, 784, 988, 1175, 1568,
            330, 440, 494, 659, 784, 988, 1175, 1568,
            330, 440, 494, 659, 784, 988, 1175, 1760,
            330, 440, 494, 659, 784, 988, 1175, 1568]

def play_moog_city():
    green = 255
    for _ in range(3):
        for note in moog_city:
            rgb.color = (0, green, 0)
            speaker.play(note, 0.15)
            green = (green - 40) % 255
    rgb.off()
    
def beautiful_buzzer_polyphony():
    for _ in range(50):
        for note in moog_city:
            speaker.play(note, 0.01)
    
play_moog_city()
beautiful_buzzer_polyphony()

# template for "Stopwatch: The Game"
import simplegui

# define global variables
message = "0:00.0"
position = [50, 50]
interval = 100
time = 0
success = 0
stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m = t // 600
    s = t/10 % 60
    ml = t % 10
    return "%d:%02d:%d" % (m, s, ml)


def update_tally():
    global stops, success
    total_stops.set_text("Stops: %d" % stops)
    total_successes.set_text("Successes: %d" % success)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global success, stops
    timer.stop()
    stops += 1

    if time % 10 == 0:
        success += 1

    update_tally()


def reset():
    global time, success, stops
    timer.stop()

    success = 0
    stops = 0
    update_tally()

    time = -1
    tick()


# define event handler for timer with 0.1 sec interval
def tick():
    global message, time
    time += 1
    message = format(time)

    # If 10 minutes elapse, reset
    if time == 6000:
        reset()


# define draw handler
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")


# create frame
f = simplegui.create_frame("Stopwatch", 500, 300)
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)
total_successes = f.add_label("Successes:")
total_stops = f.add_label("Stops:")
update_tally()

# register event handlers
f.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
f.start()


# Please remember to review the grading rubric


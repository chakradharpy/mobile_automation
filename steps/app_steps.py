
from behave import when, then


@when('I log in with PIN "{pin}"')
def step_login(context, pin):
    context.app_page.login(pin)

@when('I navigate to "Test automation project"')
def step_navigate_to_project(context):
    context.app_page.navigate_to_project()

@when('I switch to the "{tab_name}" tab')
def step_switch_tab(context, tab_name):
    context.app_page.switch_tab(tab_name)

@when('I switch back to the "Videos" tab')
def step_switch_to_videos_tab(context):
    context.app_page.switch_tab("Videos")

@when('I play the video')
def step_play_video(context):
    context.app_page.play_video()

@then('I should be able to pause the video')
def step_pause_video(context):
    context.app_page.pause_video()

@then('I replay the video using the Continue Watching button')
def step_replay_video(context):
    context.app_page.replay_video()


@then('I pause the video and navigate back')
def step_pause_and_navigate_back(context):
    context.app_page.pause_video()
    context.app_page.navigate_back()


@then('I log out of the app')
def step_logout(context):
    context.app_page.logout()

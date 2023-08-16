from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
GET /albums
"""
def test_get_all_albums(page, test_web_address, db_connection):
    # Given a GET reqest
    # It returns a list of all current albums
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        'Title: Doolittle\nReleased: 1989',
        'Title: Surfer Rosa\nReleased: 1988',
        'Title: Waterloo\nReleased: 1974',
        'Title: Super Trouper\nReleased: 1980',
        'Title: Bossanova\nReleased: 1990',
        'Title: Lover\nReleased: 2019',
        'Title: Folklore\nReleased: 2020',
        'Title: I Put a Spell on You\nReleased: 1965',
        'Title: Baltimore\nReleased: 1978',
        'Title: Here Comes the Sun\nReleased: 1971',
        'Title: Fodder on My Wings\nReleased: 1982',
        'Title: Ring Ring\nReleased: 1973'
    ])


# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

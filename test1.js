const { Builder, By, Key, until } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

async function runTest() {
  // Set up the WebDriver with Firefox
  let driver = await new Builder()
    .forBrowser('firefox')
    .setFirefoxOptions(new firefox.Options().headless(false)) // Set headless to true for a headless run
    .build();

  try {
    // Navigate to your website
    await driver.wait(until.urlIs('http://127.0.0.1:5000/'), 10000);


    // Wait for the search box to be present with an increased timeout
    let searchBox = await driver.wait(until.elementLocated(By.name('q')), 10000);

    // Interact with the search box
    await searchBox.sendKeys('Selenium', Key.RETURN);

    // Wait for a specific condition (e.g., title to be a certain value)
    await driver.wait(until.titleIs('Selenium - Google Search'), 5000);

    // Additional actions can be added here

  } finally {
    // Optionally, you can close the browser here
    // await driver.quit();
  }
}

// Call the asynchronous function
runTest();

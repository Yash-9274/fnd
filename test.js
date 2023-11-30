const { Builder, By, Key, until } = require('selenium-webdriver');

async function runTest() {
  // Set up the WebDriver with Chrome
  let driver = await new Builder()
    .forBrowser('chrome')
    .build();

  try {
    // Navigate to your website
    await driver.get('http://127.0.0.1:5000/');

    // Wait for the search box to be present
    let searchBox = await driver.wait(until.elementLocated(By.name('q')), 5000);

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

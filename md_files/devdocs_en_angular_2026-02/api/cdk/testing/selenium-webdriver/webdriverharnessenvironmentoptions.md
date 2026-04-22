# WebDriverHarnessEnvironmentOptions

WebDriverHarnessEnvironmentOptions



# WebDriverHarnessEnvironmentOptions

Options to configure the environment.

## API

```
interface WebDriverHarnessEnvironmentOptions {
  queryFn: (selector: string, root: () => webdriver.WebElement) => Promise<webdriver.WebElement[]>;
}
```

### queryFn

`(selector: string, root: () => webdriver.WebElement) => Promise<webdriver.WebElement[]>`

The query function used to find DOM elements.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/selenium-webdriver/WebDriverHarnessEnvironmentOptions>

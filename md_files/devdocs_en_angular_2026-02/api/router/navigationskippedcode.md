# NavigationSkippedCode

NavigationSkippedCode



# NavigationSkippedCode

A code for the [`NavigationSkipped`](navigationskipped) event of the [`Router`](router) to indicate the reason a navigation was skipped.

## API

```
enum NavigationSkippedCode {
  IgnoredSameUrlNavigation: NavigationSkippedCode.IgnoredSameUrlNavigation;
  IgnoredByUrlHandlingStrategy: NavigationSkippedCode.IgnoredByUrlHandlingStrategy;
}
```

### IgnoredSameUrlNavigation

A navigation was skipped because the navigation URL was the same as the current Router URL.

### IgnoredByUrlHandlingStrategy

A navigation was skipped because the configured [`UrlHandlingStrategy`](urlhandlingstrategy) return `false` for both the current Router URL and the target of the navigation.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NavigationSkippedCode>

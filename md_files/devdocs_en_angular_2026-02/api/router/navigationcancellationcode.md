# NavigationCancellationCode

NavigationCancellationCode



# NavigationCancellationCode

A code for the [`NavigationCancel`](navigationcancel) event of the [`Router`](router) to indicate the reason a navigation failed.

## API

```
enum NavigationCancellationCode {
  Redirect: NavigationCancellationCode.Redirect;
  SupersededByNewNavigation: NavigationCancellationCode.SupersededByNewNavigation;
  NoDataFromResolver: NavigationCancellationCode.NoDataFromResolver;
  GuardRejected: NavigationCancellationCode.GuardRejected;
  Aborted: NavigationCancellationCode.Aborted;
}
```

### Redirect

A navigation failed because a guard returned a [`UrlTree`](urltree) to redirect.

### SupersededByNewNavigation

A navigation failed because a more recent navigation started.

### NoDataFromResolver

A navigation failed because one of the resolvers completed without emitting a value.

### GuardRejected

A navigation failed because a guard returned `false`.

### Aborted

A navigation was aborted by the [`Navigation.abort`](navigation#abort) function.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NavigationCancellationCode>

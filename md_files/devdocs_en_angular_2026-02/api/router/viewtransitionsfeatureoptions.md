# ViewTransitionsFeatureOptions

ViewTransitionsFeatureOptions



# ViewTransitionsFeatureOptions

Options to configure the View Transitions integration in the Router.

## API

```
interface ViewTransitionsFeatureOptions {
  skipInitialTransition?: boolean | undefined;
  onViewTransitionCreated?: ((transitionInfo: ViewTransitionInfo) => void) | undefined;
}
```

### skipInitialTransition

`boolean | undefined`

Skips the very first call to `startViewTransition`. This can be useful for disabling the animation during the application's initial loading phase.

### onViewTransitionCreated

`((transitionInfo: ViewTransitionInfo) => void) | undefined`

A function to run after the `ViewTransition` is created.

This function is run in an injection context and can use [`inject`](../core/inject).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ViewTransitionsFeatureOptions>

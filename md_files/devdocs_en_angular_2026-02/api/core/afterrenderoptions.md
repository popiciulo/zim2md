# AfterRenderOptions

AfterRenderOptions



# AfterRenderOptions

Options passed to [`afterEveryRender`](aftereveryrender) and [`afterNextRender`](afternextrender).

## API

```
interface AfterRenderOptions {
  injector?: Injector | undefined;
  manualCleanup?: boolean | undefined;
}
```

### injector

`Injector | undefined`

The [`Injector`](injector) to use during creation.

If this is not provided, the current injection context will be used instead (via [`inject`](inject)).

### manualCleanup

`boolean | undefined`

Whether the hook should require manual cleanup.

If this is `false` (the default) the hook will automatically register itself to be cleaned up with the current [`DestroyRef`](destroyref).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/AfterRenderOptions>

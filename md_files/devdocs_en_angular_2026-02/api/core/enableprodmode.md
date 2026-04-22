# enableProdMode

enableProdMode



# enableProdMode

Disable Angular's development mode, which turns off assertions and other checks within the framework.

[ng build](../../cli/build)

## API

```
function enableProdMode(): void;
```

### enableProdMode

`void`

Disable Angular's development mode, which turns off assertions and other checks within the framework.

One important assertion this disables verifies that a change detection pass does not result in additional changes to any bindings (also known as unidirectional data flow).

Using this method is discouraged as the Angular CLI will set production mode when using the `optimization` option.

@returns`void`

## Description

Disable Angular's development mode, which turns off assertions and other checks within the framework.

One important assertion this disables verifies that a change detection pass does not result in additional changes to any bindings (also known as unidirectional data flow).

Using this method is discouraged as the Angular CLI will set production mode when using the `optimization` option.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/enableProdMode>

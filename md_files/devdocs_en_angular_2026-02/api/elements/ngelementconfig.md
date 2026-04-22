# NgElementConfig

NgElementConfig



# NgElementConfig

A configuration that initializes an NgElementConstructor with the dependencies and strategy it needs to transform a component into a custom element class.

## API

```
interface NgElementConfig {
  injector: Injector;
  strategyFactory?: NgElementStrategyFactory | undefined;
}
```

### injector

`Injector`

The injector to use for retrieving the component's factory.

### strategyFactory

`NgElementStrategyFactory | undefined`

An optional custom strategy factory to use instead of the default. The strategy controls how the transformation is performed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/elements/NgElementConfig>

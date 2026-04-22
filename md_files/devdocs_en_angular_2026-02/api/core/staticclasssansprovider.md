# StaticClassSansProvider

StaticClassSansProvider



# StaticClassSansProvider

Configures the [`Injector`](injector) to return an instance of `useClass` for a token. Base for [`StaticClassProvider`](staticclassprovider) decorator.

## API

```
interface StaticClassSansProvider {
  useClass: Type<any>;
  deps: any[];
}
```

### useClass

`Type<any>`

An optional class to instantiate for the `token`. By default, the `provide` class is instantiated.

### deps

`any[]`

A list of `token`s to be resolved by the injector. The list of values is then used as arguments to the `useClass` constructor.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/StaticClassSansProvider>

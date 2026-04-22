# NgElementStrategy

NgElementStrategy



# NgElementStrategy

Underlying strategy used by the NgElement to create/destroy the component and react to input changes.

## API

```
interface NgElementStrategy {
  events: Observable<NgElementStrategyEvent>;
  connect(element: HTMLElement): void;
  disconnect(): void;
  getInputValue(propName: string): any;
  setInputValue(propName: string, value: string, transform?: ((value: any) => any) | undefined): void;
}
```

### events

`Observable<NgElementStrategyEvent>`

### connect

`void`

@paramelement`HTMLElement`

@returns`void`

### disconnect

`void`

@returns`void`

### getInputValue

`any`

@parampropName`string`

@returns`any`

### setInputValue

`void`

@parampropName`string`

@paramvalue`string`

@paramtransform`((value: any) => any) | undefined`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/elements/NgElementStrategy>

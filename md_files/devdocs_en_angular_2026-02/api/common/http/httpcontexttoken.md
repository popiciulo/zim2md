# HttpContextToken

HttpContextToken



# HttpContextToken

A token used to manipulate and access values stored in [`HttpContext`](httpcontext).

[Request and response metadata](../../../guide/http/interceptors#request-and-response-metadata)

## API

```
class HttpContextToken<T> {
  constructor(defaultValue: () => T): HttpContextToken<T>;
  readonly override defaultValue: () => T;
}
```

### constructor

`HttpContextToken<T>`

@paramdefaultValue`() => T`

@returns`HttpContextToken<T>`

### defaultValue

`() => T`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpContextToken>

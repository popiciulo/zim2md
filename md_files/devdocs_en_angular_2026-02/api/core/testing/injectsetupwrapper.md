# InjectSetupWrapper

InjectSetupWrapper



# InjectSetupWrapper

## API

```
class InjectSetupWrapper {
  constructor(_moduleDef: () => TestModuleMetadata): InjectSetupWrapper;
  inject(tokens: any[], fn: Function): () => any;
}
```

### constructor

`InjectSetupWrapper`

@param\_moduleDef`() => TestModuleMetadata`

@returns`InjectSetupWrapper`

### inject

`() => any`

@paramtokens`any[]`

@paramfn`Function`

@returns`() => any`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/InjectSetupWrapper>

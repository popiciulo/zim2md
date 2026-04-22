# DeferBlockFixture

DeferBlockFixture



# DeferBlockFixture

Represents an individual defer block for testing purposes.

## API

```
class DeferBlockFixture {
  render(state: DeferBlockState): Promise<void>;
  getDeferBlocks(): Promise<DeferBlockFixture[]>;
}
```

### render

`Promise<void>`

Renders the specified state of the defer fixture.

@paramstate`DeferBlockState`

the defer state to render

@returns`Promise<void>`

### getDeferBlocks

`Promise<DeferBlockFixture[]>`

Retrieves all nested child defer block fixtures in a given defer block.

@returns`Promise<DeferBlockFixture[]>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/DeferBlockFixture>

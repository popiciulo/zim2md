# HostAttributeToken

HostAttributeToken



# HostAttributeToken

Creates a token that can be used to inject static attributes of the host node.

[Injecting host element attributes](../../guide/components/host-elements#injecting-host-element-attributes)

## API

```
class HostAttributeToken {
  constructor(attributeName: string): HostAttributeToken;
  toString(): string;
}
```

### constructor

`HostAttributeToken`

@paramattributeName`string`

@returns`HostAttributeToken`

### toString

`string`

@returns`string`

## Usage Notes

### Injecting an attribute that is known to exist

```
@Directive()
class MyDir {
  attr: string = inject(new HostAttributeToken('some-attr'));
}
```

### Optionally injecting an attribute

```
@Directive()
class MyDir {
  attr: string | null = inject(new HostAttributeToken('some-attr'), {optional: true});
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/HostAttributeToken>

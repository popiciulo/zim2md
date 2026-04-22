# HOST_TAG_NAME

HOST\_TAG\_NAME



# HOST\_TAG\_NAME

A token that can be used to inject the tag name of the host node.

## API

```
const HOST_TAG_NAME: InjectionToken<string>;
```

## Usage Notes

### Injecting a tag name that is known to exist

```
@Directive()
class MyDir {
  tagName: string = inject(HOST_TAG_NAME);
}
```

### Optionally injecting a tag name

```
@Directive()
class MyDir {
  tagName: string | null = inject(HOST_TAG_NAME, {optional: true});
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/HOST_TAG_NAME>

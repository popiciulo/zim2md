# DefaultUrlSerializer

DefaultUrlSerializer



# DefaultUrlSerializer

A default implementation of the [`UrlSerializer`](urlserializer).

## API

```
class DefaultUrlSerializer implements UrlSerializer {
  parse(url: string): UrlTree;
  serialize(tree: UrlTree): string;
}
```

### parse

`UrlTree`

Parses a url into a [`UrlTree`](urltree)

@paramurl`string`

@returns`UrlTree`

### serialize

`string`

Converts a [`UrlTree`](urltree) into a url

@paramtree`UrlTree`

@returns`string`

## Description

A default implementation of the [`UrlSerializer`](urlserializer).

Example URLs:

```
/inbox/33(popup:compose)
/inbox/33;open=true/messages/44
```

DefaultUrlSerializer uses parentheses to serialize secondary segments (e.g., popup:compose), the colon syntax to specify the outlet, and the ';parameter=value' syntax (e.g., open=true) to specify route specific parameters.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/DefaultUrlSerializer>

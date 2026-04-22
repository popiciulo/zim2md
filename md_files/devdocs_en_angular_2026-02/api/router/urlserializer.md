# UrlSerializer

UrlSerializer



# UrlSerializer

Serializes and deserializes a URL string into a URL tree.

## API

```
abstract class UrlSerializer {
  abstract parse(url: string): UrlTree;
  abstract serialize(tree: UrlTree): string;
}
```

### parse

`UrlTree`

Parse a url into a [`UrlTree`](urltree)

@paramurl`string`

@returns`UrlTree`

### serialize

`string`

Converts a [`UrlTree`](urltree) into a url

@paramtree`UrlTree`

@returns`string`

## Description

Serializes and deserializes a URL string into a URL tree.

The url serialization strategy is customizable. You can make all URLs case insensitive by providing a custom UrlSerializer.

See [`DefaultUrlSerializer`](defaulturlserializer) for an example of a URL serializer.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlSerializer>

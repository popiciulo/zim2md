# MetaDefinition

MetaDefinition



# MetaDefinition

Represents the attributes of an HTML `<meta>` element. The element itself is represented by the internal `HTMLMetaElement`.

[HTML meta tag](https://developer.mozilla.org/docs/Web/HTML/Element/meta)[Meta](meta)

## API

```
type MetaDefinition = {
  charset?: string;
  content?: string;
  httpEquiv?: string;
  id?: string;
  itemprop?: string;
  name?: string;
  property?: string;
  scheme?: string;
  url?: string;
} & {
  // TODO(IgorMinar): this type looks wrong
  [prop: string]: string;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/MetaDefinition>

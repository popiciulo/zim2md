# LocationUpgradeConfig

LocationUpgradeConfig



# LocationUpgradeConfig

Configuration options for LocationUpgrade.

## API

```
interface LocationUpgradeConfig {
  useHash?: boolean | undefined;
  hashPrefix?: string | undefined;
  urlCodec?: typeof UrlCodec | undefined;
  serverBaseHref?: string | undefined;
  appBaseHref?: string | undefined;
}
```

### useHash

`boolean | undefined`

Configures whether the location upgrade module should use the `HashLocationStrategy` or the `PathLocationStrategy`

### hashPrefix

`string | undefined`

Configures the hash prefix used in the URL when using the `HashLocationStrategy`

### urlCodec

`typeof UrlCodec | undefined`

Configures the URL codec for encoding and decoding URLs. Default is the `AngularJSCodec`

### serverBaseHref

`string | undefined`

Configures the base href when used in server-side rendered applications

### appBaseHref

`string | undefined`

Configures the base href when used in client-side rendered applications

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/upgrade/LocationUpgradeConfig>

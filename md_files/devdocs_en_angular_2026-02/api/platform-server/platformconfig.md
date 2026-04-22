# PlatformConfig

PlatformConfig



# PlatformConfig

Config object passed to initialize the platform.

## API

```
interface PlatformConfig {
  document?: string | undefined;
  url?: string | undefined;
}
```

### document

`string | undefined`

The initial DOM to use to bootstrap the server application. @default create a new DOM using Domino

### url

`string | undefined`

The URL for the current application state. This is used for initializing the platform's location. `protocol`, `hostname`, and `port` will be overridden if `baseUrl` is set. @default none

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-server/PlatformConfig>

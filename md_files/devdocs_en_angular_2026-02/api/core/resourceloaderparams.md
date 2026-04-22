# ResourceLoaderParams

ResourceLoaderParams



# ResourceLoaderParams

Parameter to a [`ResourceLoader`](resourceloader) which gives the request and other options for the current loading operation.

## API

```
interface ResourceLoaderParams<R> {
  params: NoInfer<Exclude<R, undefined>>;
  abortSignal: AbortSignal;
  previous: { status: ResourceStatus; };
}
```

### params

`NoInfer<Exclude<R, undefined>>`

### abortSignal

`AbortSignal`

### previous

`{ status: ResourceStatus; }`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ResourceLoaderParams>

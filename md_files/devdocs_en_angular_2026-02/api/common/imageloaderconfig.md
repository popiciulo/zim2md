# ImageLoaderConfig

ImageLoaderConfig



# ImageLoaderConfig

Config options recognized by the image loader function.

[ImageLoader](imageloader)[NgOptimizedImage](ngoptimizedimage)

## API

```
interface ImageLoaderConfig {
  src: string;
  width?: number | undefined;
  isPlaceholder?: boolean | undefined;
  loaderParams?: { [key: string]: any; } | undefined;
}
```

### src

`string`

Image file name to be added to the image request URL.

### width

`number | undefined`

Width of the requested image (to be used when generating srcset).

### isPlaceholder

`boolean | undefined`

Whether the loader should generate a URL for a small image placeholder instead of a full-sized image.

### loaderParams

`{ [key: string]: any; } | undefined`

Additional user-provided parameters for use by the ImageLoader.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/ImageLoaderConfig>

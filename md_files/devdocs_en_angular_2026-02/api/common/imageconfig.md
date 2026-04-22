# ImageConfig

ImageConfig



# ImageConfig

A configuration object for the image-related options. Contains:

- breakpoints: An array of integer breakpoints used to generate srcsets for responsive images.
- disableImageSizeWarning: A boolean value. Setting this to true will disable console warnings about oversized images.
- disableImageLazyLoadWarning: A boolean value. Setting this to true will disable console warnings about LCP images configured with `loading="lazy"`. Learn more about the responsive image configuration in [the NgOptimizedImage guide](../../guide/image-optimization). Learn more about image warning options in [the related error page](https://angular.dev/errors/NG0913).

## API

```
type ImageConfig = {
  breakpoints?: number[];
  placeholderResolution?: number;
  disableImageSizeWarning?: boolean;
  disableImageLazyLoadWarning?: boolean;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/ImageConfig>

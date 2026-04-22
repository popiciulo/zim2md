# NgOptimizedImage

NgOptimizedImage



# NgOptimizedImage

Directive that improves image loading performance by enforcing best practices.

[Image Optimization Guide](../../guide/image-optimization)

## API

```
class NgOptimizedImage implements OnInit ,OnChanges {
  @Input() ngSrc: string;
  @Input() ngSrcset: string;
  @Input() sizes?: string | undefined;
  @Input() width: number | undefined;
  @Input() height: number | undefined;
  @Input() decoding?: "auto" | "sync" | "async" | undefined;
  @Input() loading?: "auto" | "lazy" | "eager" | undefined;
  @Input() priority: boolean;
  @Input() loaderParams?: { [key: string]: any; } | undefined;
  @Input() disableOptimizedSrcset: boolean;
  @Input() fill: boolean;
  @Input() placeholder?: string | boolean | undefined;
  @Input() placeholderConfig?: ImagePlaceholderConfig | undefined;
  protected generatePlaceholder(placeholderInput: string | boolean): string | boolean | null;
  protected shouldBlurPlaceholder(placeholderConfig?: ImagePlaceholderConfig | undefined): boolean;
}
```

### ngSrc

`string`

Name of the source image. Image name will be processed by the image loader and the final URL will be applied as the `src` property of the image.

### ngSrcset

`string`

A comma separated list of width or density descriptors. The image name will be taken from `ngSrc` and combined with the list of width or density descriptors to generate the final `srcset` property of the image.

Example:

```
<img ngSrc="hello.jpg" ngSrcset="100w, 200w" />  =>
<img src="path/hello.jpg" srcset="path/hello.jpg?w=100 100w, path/hello.jpg?w=200 200w" />
```

### sizes

`string | undefined`

The base `sizes` attribute passed through to the `<img>` element. Providing sizes causes the image to create an automatic responsive srcset.

### width

`number | undefined`

For responsive images: the intrinsic width of the image in pixels. For fixed size images: the desired rendered width of the image in pixels.

### height

`number | undefined`

For responsive images: the intrinsic height of the image in pixels. For fixed size images: the desired rendered height of the image in pixels.

### decoding

`"auto" | "sync" | "async" | undefined`

The desired decoding behavior for the image. Defaults to `auto` if not explicitly set, matching native browser behavior.

Use `async` to decode the image off the main thread (non-blocking), `sync` for immediate decoding (blocking), or `auto` to let the browser decide the optimal strategy.

[Spec](https://html.spec.whatwg.org/multipage/images.html#image-decoding-hint)

### loading

`"auto" | "lazy" | "eager" | undefined`

The desired loading behavior (lazy, eager, or auto). Defaults to `lazy`, which is recommended for most images.

Warning: Setting images as loading="eager" or loading="auto" marks them as non-priority images and can hurt loading performance. For images which may be the LCP element, use the `priority` attribute instead of `loading`.

### priority

`boolean`

Indicates whether this image should have a high priority.

### loaderParams

`{ [key: string]: any; } | undefined`

Data to pass through to custom loaders.

### disableOptimizedSrcset

`boolean`

Disables automatic srcset generation for this image.

### fill

`boolean`

Sets the image to "fill mode", which eliminates the height/width requirement and adds styles such that the image fills its containing element.

### placeholder

`string | boolean | undefined`

A URL or data URL for an image to be used as a placeholder while this image loads.

### placeholderConfig

`ImagePlaceholderConfig | undefined`

Configuration object for placeholder settings. Options:

- blur: Setting this to false disables the automatic CSS blur.

### generatePlaceholder

`string | boolean | null`

Returns an image url formatted for use with the CSS background-image property. Expects one of:

- A base64 encoded image, which is wrapped and passed through.
- A boolean. If true, calls the image loader to generate a small placeholder url.

@paramplaceholderInput`string | boolean`

@returns`string | boolean | null`

### shouldBlurPlaceholder

`boolean`

Determines if blur should be applied, based on an optional boolean property `blur` within the optional configuration object `placeholderConfig`.

@paramplaceholderConfig`ImagePlaceholderConfig | undefined`

@returns`boolean`

## Description

Directive that improves image loading performance by enforcing best practices.

[`NgOptimizedImage`](ngoptimizedimage) ensures that the loading of the Largest Contentful Paint (LCP) image is prioritized by:

- Automatically setting the `fetchpriority` attribute on the `<img>` tag
- Lazy loading non-priority images by default
- Automatically generating a preconnect link tag in the document head

In addition, the directive:

- Generates appropriate asset URLs if a corresponding [`ImageLoader`](imageloader) function is provided
- Automatically generates a srcset
- Requires that `width` and `height` are set
- Warns if `width` or `height` have been set incorrectly
- Warns if the image will be visually distorted when rendered

## Usage Notes

The [`NgOptimizedImage`](ngoptimizedimage) directive is marked as [standalone](../../guide/components/anatomy-of-components#using-components) and can be imported directly.

Follow the steps below to enable and use the directive:

1. Import it into the necessary NgModule or a standalone Component.
2. Optionally provide an [`ImageLoader`](imageloader) if you use an image hosting service.
3. Update the necessary `<img>` tags in templates and replace `src` attributes with `ngSrc`. Using a `ngSrc` allows the directive to control when the `src` gets set, which triggers an image download.

Step 1: import the [`NgOptimizedImage`](ngoptimizedimage) directive.

```
import { NgOptimizedImage } from '@angular/common';

// Include it into the necessary NgModule
@NgModule({
  imports: [NgOptimizedImage],
})
class AppModule {}

// ... or a standalone Component
@Component({
  imports: [NgOptimizedImage],
})
class MyStandaloneComponent {}
```

Step 2: configure a loader.

To use the **default loader**: no additional code changes are necessary. The URL returned by the generic loader will always match the value of "src". In other words, this loader applies no transformations to the resource URL and the value of the `ngSrc` attribute will be used as is.

To use an existing loader for a **third-party image service**: add the provider factory for your chosen service to the `providers` array. In the example below, the Imgix loader is used:

```
import {provideImgixLoader} from '@angular/common';

// Call the function and add the result to the `providers` array:
providers: [
  provideImgixLoader("https://my.base.url/"),
],
```

The [`NgOptimizedImage`](ngoptimizedimage) directive provides the following functions:

- [`provideCloudflareLoader`](providecloudflareloader)
- [`provideCloudinaryLoader`](providecloudinaryloader)
- [`provideImageKitLoader`](provideimagekitloader)
- [`provideImgixLoader`](provideimgixloader)

If you use a different image provider, you can create a custom loader function as described below.

To use a **custom loader**: provide your loader function as a value for the [`IMAGE_LOADER`](image_loader) DI token.

```
import {IMAGE_LOADER, ImageLoaderConfig} from '@angular/common';

// Configure the loader using the `IMAGE_LOADER` token.
providers: [
  {
     provide: IMAGE_LOADER,
     useValue: (config: ImageLoaderConfig) => {
       return `https://example.com/${config.src}-${config.width}.jpg`;
     }
  },
],
```

Step 3: update `<img>` tags in templates to use `ngSrc` instead of `src`.

```
<img ngSrc="logo.png" width="200" height="100">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgOptimizedImage>

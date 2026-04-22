# HttpParamsOptions

HttpParamsOptions



# HttpParamsOptions

Options used to construct an [`HttpParams`](httpparams) instance.

[Setting URL parameters](../../../guide/http/making-requests#setting-url-parameters)[Custom parameter encoding](../../../guide/http/making-requests#custom-parameter-encoding)

## API

```
interface HttpParamsOptions {
  fromString?: string | undefined;
  fromObject?: { [param: string]: string | number | boolean | readonly (string | number | boolean)[]; } | undefined;
  encoder?: HttpParameterCodec | undefined;
}
```

### fromString

`string | undefined`

String representation of the HTTP parameters in URL-query-string format. Mutually exclusive with `fromObject`.

### fromObject

`{ [param: string]: string | number | boolean | readonly (string | number | boolean)[]; } | undefined`

Object map of the HTTP parameters. Mutually exclusive with `fromString`.

### encoder

`HttpParameterCodec | undefined`

Encoding codec used to parse and serialize the parameters.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpParamsOptions>

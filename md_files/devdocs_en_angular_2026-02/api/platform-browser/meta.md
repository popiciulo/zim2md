# Meta

Meta



# Meta

A service for managing HTML `<meta>` tags.

[HTML meta tag](https://developer.mozilla.org/docs/Web/HTML/Element/meta)[Document.querySelector()](https://developer.mozilla.org/docs/Web/API/Document/querySelector)

## API

```
class Meta {
  constructor(_doc: any): Meta;
  addTag(tag: MetaDefinition, forceCreation?: boolean): HTMLMetaElement | null;
  addTags(tags: MetaDefinition[], forceCreation?: boolean): HTMLMetaElement[];
  getTag(attrSelector: string): HTMLMetaElement | null;
  getTags(attrSelector: string): HTMLMetaElement[];
  updateTag(tag: MetaDefinition, selector?: string | undefined): HTMLMetaElement | null;
  removeTag(attrSelector: string): void;
  removeTagElement(meta: HTMLMetaElement): void;
}
```

### constructor

`Meta`

@param\_doc`any`

@returns`Meta`

### addTag

`HTMLMetaElement | null`

Retrieves or creates a specific `<meta>` tag element in the current HTML document. In searching for an existing tag, Angular attempts to match the `name` or `property` attribute values in the provided tag definition, and verifies that all other attribute values are equal. If an existing element is found, it is returned and is not modified in any way.

@paramtag`MetaDefinition`

The definition of a `<meta>` element to match or create.

@paramforceCreation`boolean`

True to create a new element without checking whether one already exists.

@returns`HTMLMetaElement | null`

### addTags

`HTMLMetaElement[]`

Retrieves or creates a set of `<meta>` tag elements in the current HTML document. In searching for an existing tag, Angular attempts to match the `name` or `property` attribute values in the provided tag definition, and verifies that all other attribute values are equal.

@paramtags`MetaDefinition[]`

An array of tag definitions to match or create.

@paramforceCreation`boolean`

True to create new elements without checking whether they already exist.

@returns`HTMLMetaElement[]`

### getTag

`HTMLMetaElement | null`

Retrieves a `<meta>` tag element in the current HTML document.

@paramattrSelector`string`

The tag attribute and value to match against, in the format `"tag_attribute='value string'"`.

@returns`HTMLMetaElement | null`

### getTags

`HTMLMetaElement[]`

Retrieves a set of `<meta>` tag elements in the current HTML document.

@paramattrSelector`string`

The tag attribute and value to match against, in the format `"tag_attribute='value string'"`.

@returns`HTMLMetaElement[]`

### updateTag

`HTMLMetaElement | null`

Modifies an existing `<meta>` tag element in the current HTML document.

@paramtag`MetaDefinition`

The tag description with which to replace the existing tag content.

@paramselector`string | undefined`

A tag attribute and value to match against, to identify an existing tag. A string in the format `"tag_attribute=`value string`"`. If not supplied, matches a tag with the same `name` or `property` attribute value as the replacement tag.

@returns`HTMLMetaElement | null`

### removeTag

`void`

Removes an existing `<meta>` tag element from the current HTML document.

@paramattrSelector`string`

A tag attribute and value to match against, to identify an existing tag. A string in the format `"tag_attribute=`value string`"`.

@returns`void`

### removeTagElement

`void`

Removes an existing `<meta>` tag element from the current HTML document.

@parammeta`HTMLMetaElement`

The tag definition to match against to identify an existing tag.

@returns`void`

## Description

A service for managing HTML `<meta>` tags.

Properties of the [`MetaDefinition`](metadefinition) object match the attributes of the HTML `<meta>` tag. These tags define document metadata that is important for things like configuring a Content Security Policy, defining browser compatibility and security settings, setting HTTP Headers, defining rich content for social sharing, and Search Engine Optimization (SEO).

To identify specific `<meta>` tags in a document, use an attribute selection string in the format `"tag_attribute='value string'"`. For example, an `attrSelector` value of `"name='description'"` matches a tag whose `name` attribute has the value `"description"`. Selectors are used with the `querySelector()` Document method, in the format `meta[{attrSelector}]`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/Meta>

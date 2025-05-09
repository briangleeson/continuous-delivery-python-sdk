# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 3.96.0-d6dec9d7-20241008-212902

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class CdToolchainV2(BaseService):
    """The CD Toolchain V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2'
    DEFAULT_SERVICE_NAME = 'cd_toolchain'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the us-south region
        'us-east': 'https://api.us-east.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the us-east region
        'eu-de': 'https://api.eu-de.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the eu-de region
        'eu-gb': 'https://api.eu-gb.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the eu-gb region
        'jp-osa': 'https://api.jp-osa.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the jp-osa region
        'jp-tok': 'https://api.jp-tok.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the jp-tok region
        'au-syd': 'https://api.au-syd.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the au-syd region
        'ca-tor': 'https://api.ca-tor.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the ca-tor region
        'br-sao': 'https://api.br-sao.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the br-sao region
        'eu-es': 'https://api.eu-es.devops.cloud.ibm.com/toolchain/v2',  # The toolchain API endpoint in the eu-es region
    }

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'CdToolchainV2':
        """
        Return a new client for the CD Toolchain service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(authenticator)
        service.configure_service(service_name)
        return service

    @classmethod
    def get_service_url_for_region(
        cls,
        region: str,
    ) -> str:
        """
        Returns the service URL associated with the specified region.
        :param str region: a string representing the region
        :return: The service URL associated with the specified region or None
                 if no mapping for the region exists
        :rtype: str
        """
        return cls.REGIONAL_ENDPOINTS.get(region, None)

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the CD Toolchain service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Toolchains
    #########################

    def list_toolchains(
        self,
        resource_group_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of toolchains.

        Returns a list of toolchains that the caller is authorized to access and that
        meets the provided query parameters.

        :param str resource_group_id: The resource group ID where the toolchains
               exist.
        :param int limit: (optional) Limit the number of results.
        :param str start: (optional) Pagination token.
        :param str name: (optional) Exact name of toolchain to look up. This
               parameter is case sensitive.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainCollection` object
        """

        if not resource_group_id:
            raise ValueError('resource_group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_toolchains',
        )
        headers.update(sdk_headers)

        params = {
            'resource_group_id': resource_group_id,
            'limit': limit,
            'start': start,
            'name': name,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/toolchains'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_toolchain(
        self,
        name: str,
        resource_group_id: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a toolchain.

        Creates a new toolchain based off the provided parameters in the body.

        :param str name: Toolchain name.
        :param str resource_group_id: Resource group where toolchain will be
               created.
        :param str description: (optional) Describes the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainPost` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if resource_group_id is None:
            raise ValueError('resource_group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_toolchain',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'resource_group_id': resource_group_id,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/toolchains'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_toolchain_by_id(
        self,
        toolchain_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a toolchain.

        Returns data for a single toolchain identified by its ID.

        :param str toolchain_id: ID of the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Toolchain` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_toolchain_by_id',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_toolchain(
        self,
        toolchain_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a toolchain.

        Delete the toolchain with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_toolchain',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_toolchain(
        self,
        toolchain_id: str,
        toolchain_prototype_patch: 'ToolchainPrototypePatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a toolchain.

        Update the toolchain with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param ToolchainPrototypePatch toolchain_prototype_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainPatch` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if toolchain_prototype_patch is None:
            raise ValueError('toolchain_prototype_patch must be provided')
        if isinstance(toolchain_prototype_patch, ToolchainPrototypePatch):
            toolchain_prototype_patch = convert_model(toolchain_prototype_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_toolchain',
        )
        headers.update(sdk_headers)

        data = json.dumps(toolchain_prototype_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_toolchain_event(
        self,
        toolchain_id: str,
        title: str,
        description: str,
        content_type: str,
        *,
        data: Optional['ToolchainEventPrototypeData'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a toolchain event.

        Creates and sends a custom event to each Event Notifications instance configured
        as a tool into the toolchain. This operation will fail if no Event Notifications
        instances are configured into the toolchain.

        :param str toolchain_id: ID of the toolchain to send events from.
        :param str title: Event title.
        :param str description: Describes the event.
        :param str content_type: The content type of the attached data. Supported
               values are `text/plain`, `application/json`, and `none`.
        :param ToolchainEventPrototypeData data: (optional) Additional data to be
               added with the event. The format must correspond to the value of
               `content_type`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainEventPost` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if title is None:
            raise ValueError('title must be provided')
        if description is None:
            raise ValueError('description must be provided')
        if content_type is None:
            raise ValueError('content_type must be provided')
        if data is not None:
            data = convert_model(data)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_toolchain_event',
        )
        headers.update(sdk_headers)

        data = {
            'title': title,
            'description': description,
            'content_type': content_type,
            'data': data,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/events'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Tools
    #########################

    def list_tools(
        self,
        toolchain_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of tools bound to a toolchain.

        Returns a list of tools bound to a toolchain that the caller is authorized to
        access and that meet the provided query parameters.

        :param str toolchain_id: ID of the toolchain that tools are bound to.
        :param int limit: (optional) Limit the number of results.
        :param str start: (optional) Pagination token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainToolCollection` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_tools',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_tool(
        self,
        toolchain_id: str,
        tool_type_id: str,
        *,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a tool.

        Provisions a new tool based off the provided parameters in the body and binds it
        to the specified toolchain.

        :param str toolchain_id: ID of the toolchain to bind the tool to.
        :param str tool_type_id: The unique short name of the tool that should be
               provisioned. A table of `tool_type_id` values corresponding to each tool
               integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str name: (optional) Name of the tool.
        :param dict parameters: (optional) Unique key-value pairs representing
               parameters to be used to create the tool. A list of parameters for each
               tool integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainToolPost` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if tool_type_id is None:
            raise ValueError('tool_type_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tool',
        )
        headers.update(sdk_headers)

        data = {
            'tool_type_id': tool_type_id,
            'name': name,
            'parameters': parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tool_by_id(
        self,
        toolchain_id: str,
        tool_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a tool.

        Returns a tool that is bound to the provided toolchain.

        :param str toolchain_id: ID of the toolchain.
        :param str tool_id: ID of the tool bound to the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainTool` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if not tool_id:
            raise ValueError('tool_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tool_by_id',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id', 'tool_id']
        path_param_values = self.encode_path_vars(toolchain_id, tool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools/{tool_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tool(
        self,
        toolchain_id: str,
        tool_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a tool.

        Delete the tool with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param str tool_id: ID of the tool bound to the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if not tool_id:
            raise ValueError('tool_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tool',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['toolchain_id', 'tool_id']
        path_param_values = self.encode_path_vars(toolchain_id, tool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools/{tool_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_tool(
        self,
        toolchain_id: str,
        tool_id: str,
        toolchain_tool_prototype_patch: 'ToolchainToolPrototypePatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a tool.

        Update the tool with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param str tool_id: ID of the tool bound to the toolchain.
        :param ToolchainToolPrototypePatch toolchain_tool_prototype_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainToolPatch` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if not tool_id:
            raise ValueError('tool_id must be provided')
        if toolchain_tool_prototype_patch is None:
            raise ValueError('toolchain_tool_prototype_patch must be provided')
        if isinstance(toolchain_tool_prototype_patch, ToolchainToolPrototypePatch):
            toolchain_tool_prototype_patch = convert_model(toolchain_tool_prototype_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_tool',
        )
        headers.update(sdk_headers)

        data = json.dumps(toolchain_tool_prototype_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id', 'tool_id']
        path_param_values = self.encode_path_vars(toolchain_id, tool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools/{tool_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class ToolModel:
    """
    Model describing tool resource.

    :param str id: Tool ID.
    :param str resource_group_id: Resource group where the tool is located.
    :param str crn: Tool CRN.
    :param str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str toolchain_id: ID of toolchain which the tool is bound to.
    :param str toolchain_crn: CRN of toolchain which the tool is bound to.
    :param str href: URI representing the tool.
    :param ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :param str name: (optional) Name of the tool.
    :param datetime updated_at: Latest tool update timestamp.
    :param dict parameters: Unique key-value pairs representing parameters to be
          used to create the tool. A list of parameters for each tool integration can be
          found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str state: Current configuration state of the tool.
    """

    def __init__(
        self,
        id: str,
        resource_group_id: str,
        crn: str,
        tool_type_id: str,
        toolchain_id: str,
        toolchain_crn: str,
        href: str,
        referent: 'ToolModelReferent',
        updated_at: datetime,
        parameters: dict,
        state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolModel object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Name of the tool.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolModel':
        """Initialize a ToolModel object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolModel JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolModel JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolModel JSON')
        if (tool_type_id := _dict.get('tool_type_id')) is not None:
            args['tool_type_id'] = tool_type_id
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolModel JSON')
        if (toolchain_id := _dict.get('toolchain_id')) is not None:
            args['toolchain_id'] = toolchain_id
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolModel JSON')
        if (toolchain_crn := _dict.get('toolchain_crn')) is not None:
            args['toolchain_crn'] = toolchain_crn
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolModel JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolModel JSON')
        if (referent := _dict.get('referent')) is not None:
            args['referent'] = ToolModelReferent.from_dict(referent)
        else:
            raise ValueError('Required property \'referent\' not present in ToolModel JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolModel JSON')
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = parameters
        else:
            raise ValueError('Required property \'parameters\' not present in ToolModel JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in ToolModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            if isinstance(self.referent, dict):
                _dict['referent'] = self.referent
            else:
                _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """

        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolModelReferent:
    """
    Information on URIs to access this resource through the UI or API.

    :param str ui_href: (optional) URI representing this resource through the UI.
    :param str api_href: (optional) URI representing this resource through an API.
    """

    def __init__(
        self,
        *,
        ui_href: Optional[str] = None,
        api_href: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolModelReferent object.

        :param str ui_href: (optional) URI representing this resource through the
               UI.
        :param str api_href: (optional) URI representing this resource through an
               API.
        """
        self.ui_href = ui_href
        self.api_href = api_href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolModelReferent':
        """Initialize a ToolModelReferent object from a json dictionary."""
        args = {}
        if (ui_href := _dict.get('ui_href')) is not None:
            args['ui_href'] = ui_href
        if (api_href := _dict.get('api_href')) is not None:
            args['api_href'] = api_href
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolModelReferent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'api_href') and self.api_href is not None:
            _dict['api_href'] = self.api_href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolModelReferent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolModelReferent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolModelReferent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Toolchain:
    """
    Response structure for GET toolchains.

    :param str id: Toolchain ID.
    :param str name: Toolchain name.
    :param str description: Describes the toolchain.
    :param str account_id: Account ID where toolchain can be found.
    :param str location: Toolchain region.
    :param str resource_group_id: Resource group where the toolchain is located.
    :param str crn: Toolchain CRN.
    :param str href: URI that can be used to retrieve toolchain.
    :param str ui_href: URL of a user-facing user interface for this toolchain.
    :param datetime created_at: Toolchain creation timestamp.
    :param datetime updated_at: Latest toolchain update timestamp.
    :param str created_by: Identity that created the toolchain.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        account_id: str,
        location: str,
        resource_group_id: str,
        crn: str,
        href: str,
        ui_href: str,
        created_at: datetime,
        updated_at: datetime,
        created_by: str,
    ) -> None:
        """
        Initialize a Toolchain object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Describes the toolchain.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Toolchain':
        """Initialize a Toolchain object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Toolchain JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Toolchain JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in Toolchain JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in Toolchain JSON')
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        else:
            raise ValueError('Required property \'location\' not present in Toolchain JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in Toolchain JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in Toolchain JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in Toolchain JSON')
        if (ui_href := _dict.get('ui_href')) is not None:
            args['ui_href'] = ui_href
        else:
            raise ValueError('Required property \'ui_href\' not present in Toolchain JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in Toolchain JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in Toolchain JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in Toolchain JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Toolchain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Toolchain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Toolchain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Toolchain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainCollection:
    """
    Response structure for GET toolchains.

    :param int total_count: Total number of toolchains found in collection.
    :param int limit: Maximum number of toolchains returned from collection.
    :param ToolchainCollectionFirst first: Information about retrieving first
          toolchain results from the collection.
    :param ToolchainCollectionPrevious previous: (optional) Information about
          retrieving previous toolchain results from the collection.
    :param ToolchainCollectionNext next: (optional) Information about retrieving
          next toolchain results from the collection.
    :param ToolchainCollectionLast last: Information about retrieving last toolchain
          results from the collection.
    :param List[ToolchainModel] toolchains: (optional) Toolchain results returned
          from the collection.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'ToolchainCollectionFirst',
        last: 'ToolchainCollectionLast',
        *,
        previous: Optional['ToolchainCollectionPrevious'] = None,
        next: Optional['ToolchainCollectionNext'] = None,
        toolchains: Optional[List['ToolchainModel']] = None,
    ) -> None:
        """
        Initialize a ToolchainCollection object.

        :param int total_count: Total number of toolchains found in collection.
        :param int limit: Maximum number of toolchains returned from collection.
        :param ToolchainCollectionFirst first: Information about retrieving first
               toolchain results from the collection.
        :param ToolchainCollectionLast last: Information about retrieving last
               toolchain results from the collection.
        :param ToolchainCollectionPrevious previous: (optional) Information about
               retrieving previous toolchain results from the collection.
        :param ToolchainCollectionNext next: (optional) Information about
               retrieving next toolchain results from the collection.
        :param List[ToolchainModel] toolchains: (optional) Toolchain results
               returned from the collection.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.toolchains = toolchains

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollection':
        """Initialize a ToolchainCollection object from a json dictionary."""
        args = {}
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ToolchainCollection JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ToolchainCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ToolchainCollectionFirst.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in ToolchainCollection JSON')
        if (previous := _dict.get('previous')) is not None:
            args['previous'] = ToolchainCollectionPrevious.from_dict(previous)
        if (next := _dict.get('next')) is not None:
            args['next'] = ToolchainCollectionNext.from_dict(next)
        if (last := _dict.get('last')) is not None:
            args['last'] = ToolchainCollectionLast.from_dict(last)
        else:
            raise ValueError('Required property \'last\' not present in ToolchainCollection JSON')
        if (toolchains := _dict.get('toolchains')) is not None:
            args['toolchains'] = [ToolchainModel.from_dict(v) for v in toolchains]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            if isinstance(self.previous, dict):
                _dict['previous'] = self.previous
            else:
                _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            if isinstance(self.last, dict):
                _dict['last'] = self.last
            else:
                _dict['last'] = self.last.to_dict()
        if hasattr(self, 'toolchains') and self.toolchains is not None:
            toolchains_list = []
            for v in self.toolchains:
                if isinstance(v, dict):
                    toolchains_list.append(v)
                else:
                    toolchains_list.append(v.to_dict())
            _dict['toolchains'] = toolchains_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainCollectionFirst:
    """
    Information about retrieving first toolchain results from the collection.

    :param str href: URI that can be used to get first results from the collection.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a ToolchainCollectionFirst object.

        :param str href: URI that can be used to get first results from the
               collection.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionFirst':
        """Initialize a ToolchainCollectionFirst object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainCollectionLast:
    """
    Information about retrieving last toolchain results from the collection.

    :param str start: (optional) Cursor that can be set as the 'start' query
          parameter to get the last set of toolchain collections.
    :param str href: URI that can be used to get last results from the collection.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainCollectionLast object.

        :param str href: URI that can be used to get last results from the
               collection.
        :param str start: (optional) Cursor that can be set as the 'start' query
               parameter to get the last set of toolchain collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionLast':
        """Initialize a ToolchainCollectionLast object from a json dictionary."""
        args = {}
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionLast JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionLast object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionLast object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionLast') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionLast') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainCollectionNext:
    """
    Information about retrieving next toolchain results from the collection.

    :param str start: (optional) Cursor that can be set as the 'start' query
          parameter to get the next set of toolchain collections.
    :param str href: URI that can be used to get next results from the collection.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainCollectionNext object.

        :param str href: URI that can be used to get next results from the
               collection.
        :param str start: (optional) Cursor that can be set as the 'start' query
               parameter to get the next set of toolchain collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionNext':
        """Initialize a ToolchainCollectionNext object from a json dictionary."""
        args = {}
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionNext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainCollectionPrevious:
    """
    Information about retrieving previous toolchain results from the collection.

    :param str start: (optional) Cursor that can be set as the 'start' query
          parameter to get the previous set of toolchain collections.
    :param str href: URI that can be used to get previous results from the
          collection.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainCollectionPrevious object.

        :param str href: URI that can be used to get previous results from the
               collection.
        :param str start: (optional) Cursor that can be set as the 'start' query
               parameter to get the previous set of toolchain collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionPrevious':
        """Initialize a ToolchainCollectionPrevious object from a json dictionary."""
        args = {}
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionPrevious JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionPrevious object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionPrevious object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionPrevious') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionPrevious') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainEventPost:
    """
    Response structure for POST toolchain event.

    :param str id: Event ID.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a ToolchainEventPost object.

        :param str id: Event ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainEventPost':
        """Initialize a ToolchainEventPost object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainEventPost JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainEventPost object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainEventPost object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainEventPost') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainEventPost') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainEventPrototypeData:
    """
    Additional data to be added with the event. The format must correspond to the value of
    `content_type`.

    :param ToolchainEventPrototypeDataApplicationJson application_json: (optional)
          Contains JSON data to be added with the event. `content_type` must be set to
          `application/json`.
    :param ToolchainEventPrototypeDataTextPlain text_plain: (optional) Contains text
          data to be added with the event. `content_type` must be set to `text/plain`.
    """

    def __init__(
        self,
        *,
        application_json: Optional['ToolchainEventPrototypeDataApplicationJson'] = None,
        text_plain: Optional['ToolchainEventPrototypeDataTextPlain'] = None,
    ) -> None:
        """
        Initialize a ToolchainEventPrototypeData object.

        :param ToolchainEventPrototypeDataApplicationJson application_json:
               (optional) Contains JSON data to be added with the event. `content_type`
               must be set to `application/json`.
        :param ToolchainEventPrototypeDataTextPlain text_plain: (optional) Contains
               text data to be added with the event. `content_type` must be set to
               `text/plain`.
        """
        self.application_json = application_json
        self.text_plain = text_plain

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainEventPrototypeData':
        """Initialize a ToolchainEventPrototypeData object from a json dictionary."""
        args = {}
        if (application_json := _dict.get('application_json')) is not None:
            args['application_json'] = ToolchainEventPrototypeDataApplicationJson.from_dict(application_json)
        if (text_plain := _dict.get('text_plain')) is not None:
            args['text_plain'] = ToolchainEventPrototypeDataTextPlain.from_dict(text_plain)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainEventPrototypeData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application_json') and self.application_json is not None:
            if isinstance(self.application_json, dict):
                _dict['application_json'] = self.application_json
            else:
                _dict['application_json'] = self.application_json.to_dict()
        if hasattr(self, 'text_plain') and self.text_plain is not None:
            if isinstance(self.text_plain, dict):
                _dict['text_plain'] = self.text_plain
            else:
                _dict['text_plain'] = self.text_plain.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainEventPrototypeData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainEventPrototypeData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainEventPrototypeData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainEventPrototypeDataApplicationJson:
    """
    Contains JSON data to be added with the event. `content_type` must be set to
    `application/json`.

    :param dict content: JSON-formatted key-value pairs representing any additional
          information to be included with the event. The payload is constrained to a
          maximum depth of 5, and keys that must satisfy the pattern ^[a-zA-Z0-9-_]+$.
    """

    def __init__(
        self,
        content: dict,
    ) -> None:
        """
        Initialize a ToolchainEventPrototypeDataApplicationJson object.

        :param dict content: JSON-formatted key-value pairs representing any
               additional information to be included with the event. The payload is
               constrained to a maximum depth of 5, and keys that must satisfy the pattern
               ^[a-zA-Z0-9-_]+$.
        """
        self.content = content

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainEventPrototypeDataApplicationJson':
        """Initialize a ToolchainEventPrototypeDataApplicationJson object from a json dictionary."""
        args = {}
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        else:
            raise ValueError(
                'Required property \'content\' not present in ToolchainEventPrototypeDataApplicationJson JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainEventPrototypeDataApplicationJson object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainEventPrototypeDataApplicationJson object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainEventPrototypeDataApplicationJson') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainEventPrototypeDataApplicationJson') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainEventPrototypeDataTextPlain:
    """
    Contains text data to be added with the event. `content_type` must be set to
    `text/plain`.

    :param str content: The text data to send in the event.
    """

    def __init__(
        self,
        content: str,
    ) -> None:
        """
        Initialize a ToolchainEventPrototypeDataTextPlain object.

        :param str content: The text data to send in the event.
        """
        self.content = content

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainEventPrototypeDataTextPlain':
        """Initialize a ToolchainEventPrototypeDataTextPlain object from a json dictionary."""
        args = {}
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        else:
            raise ValueError('Required property \'content\' not present in ToolchainEventPrototypeDataTextPlain JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainEventPrototypeDataTextPlain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainEventPrototypeDataTextPlain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainEventPrototypeDataTextPlain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainEventPrototypeDataTextPlain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainModel:
    """
    Model describing toolchain resource.

    :param str id: Toolchain ID.
    :param str name: Toolchain name.
    :param str description: Describes the toolchain.
    :param str account_id: Account ID where toolchain can be found.
    :param str location: Toolchain region.
    :param str resource_group_id: Resource group where the toolchain is located.
    :param str crn: Toolchain CRN.
    :param str href: URI that can be used to retrieve toolchain.
    :param str ui_href: URL of a user-facing user interface for this toolchain.
    :param datetime created_at: Toolchain creation timestamp.
    :param datetime updated_at: Latest toolchain update timestamp.
    :param str created_by: Identity that created the toolchain.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        account_id: str,
        location: str,
        resource_group_id: str,
        crn: str,
        href: str,
        ui_href: str,
        created_at: datetime,
        updated_at: datetime,
        created_by: str,
    ) -> None:
        """
        Initialize a ToolchainModel object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Describes the toolchain.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainModel':
        """Initialize a ToolchainModel object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainModel JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ToolchainModel JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ToolchainModel JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in ToolchainModel JSON')
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        else:
            raise ValueError('Required property \'location\' not present in ToolchainModel JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainModel JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainModel JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainModel JSON')
        if (ui_href := _dict.get('ui_href')) is not None:
            args['ui_href'] = ui_href
        else:
            raise ValueError('Required property \'ui_href\' not present in ToolchainModel JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in ToolchainModel JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainModel JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in ToolchainModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainPatch:
    """
    Response structure for PATCH toolchain.

    :param str id: Toolchain ID.
    :param str name: Toolchain name.
    :param str description: Describes the toolchain.
    :param str account_id: Account ID where toolchain can be found.
    :param str location: Toolchain region.
    :param str resource_group_id: Resource group where the toolchain is located.
    :param str crn: Toolchain CRN.
    :param str href: URI that can be used to retrieve toolchain.
    :param str ui_href: URL of a user-facing user interface for this toolchain.
    :param datetime created_at: Toolchain creation timestamp.
    :param datetime updated_at: Latest toolchain update timestamp.
    :param str created_by: Identity that created the toolchain.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        account_id: str,
        location: str,
        resource_group_id: str,
        crn: str,
        href: str,
        ui_href: str,
        created_at: datetime,
        updated_at: datetime,
        created_by: str,
    ) -> None:
        """
        Initialize a ToolchainPatch object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Describes the toolchain.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainPatch':
        """Initialize a ToolchainPatch object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainPatch JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ToolchainPatch JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ToolchainPatch JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in ToolchainPatch JSON')
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        else:
            raise ValueError('Required property \'location\' not present in ToolchainPatch JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainPatch JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainPatch JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainPatch JSON')
        if (ui_href := _dict.get('ui_href')) is not None:
            args['ui_href'] = ui_href
        else:
            raise ValueError('Required property \'ui_href\' not present in ToolchainPatch JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in ToolchainPatch JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainPatch JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in ToolchainPatch JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainPost:
    """
    Response structure for POST toolchain.

    :param str id: Toolchain ID.
    :param str name: Toolchain name.
    :param str description: Describes the toolchain.
    :param str account_id: Account ID where toolchain can be found.
    :param str location: Toolchain region.
    :param str resource_group_id: Resource group where the toolchain is located.
    :param str crn: Toolchain CRN.
    :param str href: URI that can be used to retrieve toolchain.
    :param str ui_href: URL of a user-facing user interface for this toolchain.
    :param datetime created_at: Toolchain creation timestamp.
    :param datetime updated_at: Latest toolchain update timestamp.
    :param str created_by: Identity that created the toolchain.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        account_id: str,
        location: str,
        resource_group_id: str,
        crn: str,
        href: str,
        ui_href: str,
        created_at: datetime,
        updated_at: datetime,
        created_by: str,
    ) -> None:
        """
        Initialize a ToolchainPost object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Describes the toolchain.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainPost':
        """Initialize a ToolchainPost object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainPost JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ToolchainPost JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ToolchainPost JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in ToolchainPost JSON')
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        else:
            raise ValueError('Required property \'location\' not present in ToolchainPost JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainPost JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainPost JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainPost JSON')
        if (ui_href := _dict.get('ui_href')) is not None:
            args['ui_href'] = ui_href
        else:
            raise ValueError('Required property \'ui_href\' not present in ToolchainPost JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in ToolchainPost JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainPost JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in ToolchainPost JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainPost object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainPost object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainPost') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainPost') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainPrototypePatch:
    """
    Body structure for the update toolchain PATCH request.

    :param str name: (optional) The name of the toolchain.
    :param str description: (optional) An optional description.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainPrototypePatch object.

        :param str name: (optional) The name of the toolchain.
        :param str description: (optional) An optional description.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainPrototypePatch':
        """Initialize a ToolchainPrototypePatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainPrototypePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainPrototypePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainPrototypePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainPrototypePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainTool:
    """
    Response structure for GET tool.

    :param str id: Tool ID.
    :param str resource_group_id: Resource group where the tool is located.
    :param str crn: Tool CRN.
    :param str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str toolchain_id: ID of toolchain which the tool is bound to.
    :param str toolchain_crn: CRN of toolchain which the tool is bound to.
    :param str href: URI representing the tool.
    :param ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :param str name: (optional) Name of the tool.
    :param datetime updated_at: Latest tool update timestamp.
    :param dict parameters: Unique key-value pairs representing parameters to be
          used to create the tool. A list of parameters for each tool integration can be
          found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str state: Current configuration state of the tool.
    """

    def __init__(
        self,
        id: str,
        resource_group_id: str,
        crn: str,
        tool_type_id: str,
        toolchain_id: str,
        toolchain_crn: str,
        href: str,
        referent: 'ToolModelReferent',
        updated_at: datetime,
        parameters: dict,
        state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainTool object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Name of the tool.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainTool':
        """Initialize a ToolchainTool object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainTool JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainTool JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainTool JSON')
        if (tool_type_id := _dict.get('tool_type_id')) is not None:
            args['tool_type_id'] = tool_type_id
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolchainTool JSON')
        if (toolchain_id := _dict.get('toolchain_id')) is not None:
            args['toolchain_id'] = toolchain_id
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolchainTool JSON')
        if (toolchain_crn := _dict.get('toolchain_crn')) is not None:
            args['toolchain_crn'] = toolchain_crn
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolchainTool JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainTool JSON')
        if (referent := _dict.get('referent')) is not None:
            args['referent'] = ToolModelReferent.from_dict(referent)
        else:
            raise ValueError('Required property \'referent\' not present in ToolchainTool JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainTool JSON')
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = parameters
        else:
            raise ValueError('Required property \'parameters\' not present in ToolchainTool JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in ToolchainTool JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainTool object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            if isinstance(self.referent, dict):
                _dict['referent'] = self.referent
            else:
                _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainTool object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainTool') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainTool') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """

        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolchainToolCollection:
    """
    Response structure for GET tools.

    :param int limit: Maximum number of tools returned from collection.
    :param int total_count: Total number of tools found in collection.
    :param ToolchainToolCollectionFirst first: Information about retrieving first
          tool results from the collection.
    :param ToolchainToolCollectionPrevious previous: (optional) Information about
          retrieving previous tool results from the collection.
    :param ToolchainToolCollectionNext next: (optional) Information about retrieving
          next tool results from the collection.
    :param ToolchainToolCollectionLast last: Information about retrieving last tool
          results from the collection.
    :param List[ToolModel] tools: Tool results returned from the collection.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        first: 'ToolchainToolCollectionFirst',
        last: 'ToolchainToolCollectionLast',
        tools: List['ToolModel'],
        *,
        previous: Optional['ToolchainToolCollectionPrevious'] = None,
        next: Optional['ToolchainToolCollectionNext'] = None,
    ) -> None:
        """
        Initialize a ToolchainToolCollection object.

        :param int limit: Maximum number of tools returned from collection.
        :param int total_count: Total number of tools found in collection.
        :param ToolchainToolCollectionFirst first: Information about retrieving
               first tool results from the collection.
        :param ToolchainToolCollectionLast last: Information about retrieving last
               tool results from the collection.
        :param List[ToolModel] tools: Tool results returned from the collection.
        :param ToolchainToolCollectionPrevious previous: (optional) Information
               about retrieving previous tool results from the collection.
        :param ToolchainToolCollectionNext next: (optional) Information about
               retrieving next tool results from the collection.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.tools = tools

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollection':
        """Initialize a ToolchainToolCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ToolchainToolCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ToolchainToolCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ToolchainToolCollectionFirst.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in ToolchainToolCollection JSON')
        if (previous := _dict.get('previous')) is not None:
            args['previous'] = ToolchainToolCollectionPrevious.from_dict(previous)
        if (next := _dict.get('next')) is not None:
            args['next'] = ToolchainToolCollectionNext.from_dict(next)
        if (last := _dict.get('last')) is not None:
            args['last'] = ToolchainToolCollectionLast.from_dict(last)
        else:
            raise ValueError('Required property \'last\' not present in ToolchainToolCollection JSON')
        if (tools := _dict.get('tools')) is not None:
            args['tools'] = [ToolModel.from_dict(v) for v in tools]
        else:
            raise ValueError('Required property \'tools\' not present in ToolchainToolCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            if isinstance(self.previous, dict):
                _dict['previous'] = self.previous
            else:
                _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            if isinstance(self.last, dict):
                _dict['last'] = self.last
            else:
                _dict['last'] = self.last.to_dict()
        if hasattr(self, 'tools') and self.tools is not None:
            tools_list = []
            for v in self.tools:
                if isinstance(v, dict):
                    tools_list.append(v)
                else:
                    tools_list.append(v.to_dict())
            _dict['tools'] = tools_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainToolCollectionFirst:
    """
    Information about retrieving first tool results from the collection.

    :param str href: URI that can be used to get first results from the collection.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a ToolchainToolCollectionFirst object.

        :param str href: URI that can be used to get first results from the
               collection.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionFirst':
        """Initialize a ToolchainToolCollectionFirst object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainToolCollectionLast:
    """
    Information about retrieving last tool results from the collection.

    :param str start: (optional) Cursor that can be used to get the last set of tool
          collections.
    :param str href: URI that can be used to get last results from the collection.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainToolCollectionLast object.

        :param str href: URI that can be used to get last results from the
               collection.
        :param str start: (optional) Cursor that can be used to get the last set of
               tool collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionLast':
        """Initialize a ToolchainToolCollectionLast object from a json dictionary."""
        args = {}
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionLast JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionLast object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionLast object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionLast') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionLast') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainToolCollectionNext:
    """
    Information about retrieving next tool results from the collection.

    :param str start: (optional) Cursor that can be used to get the next set of tool
          collections.
    :param str href: URI that can be used to get next results from the collection.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainToolCollectionNext object.

        :param str href: URI that can be used to get next results from the
               collection.
        :param str start: (optional) Cursor that can be used to get the next set of
               tool collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionNext':
        """Initialize a ToolchainToolCollectionNext object from a json dictionary."""
        args = {}
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionNext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainToolCollectionPrevious:
    """
    Information about retrieving previous tool results from the collection.

    :param str start: (optional) Cursor that can be used to get the previous set of
          tool collections.
    :param str href: URI that can be used to get previous results from the
          collection.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainToolCollectionPrevious object.

        :param str href: URI that can be used to get previous results from the
               collection.
        :param str start: (optional) Cursor that can be used to get the previous
               set of tool collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionPrevious':
        """Initialize a ToolchainToolCollectionPrevious object from a json dictionary."""
        args = {}
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionPrevious JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionPrevious object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionPrevious object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionPrevious') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionPrevious') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainToolPatch:
    """
    Response structure for PATCH tool.

    :param str id: Tool ID.
    :param str resource_group_id: Resource group where the tool is located.
    :param str crn: Tool CRN.
    :param str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str toolchain_id: ID of toolchain which the tool is bound to.
    :param str toolchain_crn: CRN of toolchain which the tool is bound to.
    :param str href: URI representing the tool.
    :param ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :param str name: (optional) Name of the tool.
    :param datetime updated_at: Latest tool update timestamp.
    :param dict parameters: Unique key-value pairs representing parameters to be
          used to create the tool. A list of parameters for each tool integration can be
          found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str state: Current configuration state of the tool.
    """

    def __init__(
        self,
        id: str,
        resource_group_id: str,
        crn: str,
        tool_type_id: str,
        toolchain_id: str,
        toolchain_crn: str,
        href: str,
        referent: 'ToolModelReferent',
        updated_at: datetime,
        parameters: dict,
        state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainToolPatch object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Name of the tool.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolPatch':
        """Initialize a ToolchainToolPatch object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainToolPatch JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainToolPatch JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainToolPatch JSON')
        if (tool_type_id := _dict.get('tool_type_id')) is not None:
            args['tool_type_id'] = tool_type_id
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolchainToolPatch JSON')
        if (toolchain_id := _dict.get('toolchain_id')) is not None:
            args['toolchain_id'] = toolchain_id
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolchainToolPatch JSON')
        if (toolchain_crn := _dict.get('toolchain_crn')) is not None:
            args['toolchain_crn'] = toolchain_crn
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolchainToolPatch JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolPatch JSON')
        if (referent := _dict.get('referent')) is not None:
            args['referent'] = ToolModelReferent.from_dict(referent)
        else:
            raise ValueError('Required property \'referent\' not present in ToolchainToolPatch JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainToolPatch JSON')
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = parameters
        else:
            raise ValueError('Required property \'parameters\' not present in ToolchainToolPatch JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in ToolchainToolPatch JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            if isinstance(self.referent, dict):
                _dict['referent'] = self.referent
            else:
                _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """

        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolchainToolPost:
    """
    POST tool response body.

    :param str id: Tool ID.
    :param str resource_group_id: Resource group where the tool is located.
    :param str crn: Tool CRN.
    :param str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str toolchain_id: ID of toolchain which the tool is bound to.
    :param str toolchain_crn: CRN of toolchain which the tool is bound to.
    :param str href: URI representing the tool.
    :param ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :param str name: (optional) Name of the tool.
    :param datetime updated_at: Latest tool update timestamp.
    :param dict parameters: Unique key-value pairs representing parameters to be
          used to create the tool. A list of parameters for each tool integration can be
          found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param str state: Current configuration state of the tool.
    """

    def __init__(
        self,
        id: str,
        resource_group_id: str,
        crn: str,
        tool_type_id: str,
        toolchain_id: str,
        toolchain_crn: str,
        href: str,
        referent: 'ToolModelReferent',
        updated_at: datetime,
        parameters: dict,
        state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ToolchainToolPost object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Name of the tool.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolPost':
        """Initialize a ToolchainToolPost object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainToolPost JSON')
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainToolPost JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainToolPost JSON')
        if (tool_type_id := _dict.get('tool_type_id')) is not None:
            args['tool_type_id'] = tool_type_id
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolchainToolPost JSON')
        if (toolchain_id := _dict.get('toolchain_id')) is not None:
            args['toolchain_id'] = toolchain_id
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolchainToolPost JSON')
        if (toolchain_crn := _dict.get('toolchain_crn')) is not None:
            args['toolchain_crn'] = toolchain_crn
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolchainToolPost JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolPost JSON')
        if (referent := _dict.get('referent')) is not None:
            args['referent'] = ToolModelReferent.from_dict(referent)
        else:
            raise ValueError('Required property \'referent\' not present in ToolchainToolPost JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainToolPost JSON')
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = parameters
        else:
            raise ValueError('Required property \'parameters\' not present in ToolchainToolPost JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in ToolchainToolPost JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolPost object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            if isinstance(self.referent, dict):
                _dict['referent'] = self.referent
            else:
                _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolPost object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolPost') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolPost') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """

        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolchainToolPrototypePatch:
    """
    Details on the new tool.

    :param str name: (optional) Name of the tool.
    :param str tool_type_id: (optional) The unique short name of the tool that
          should be provisioned or updated. A table of `tool_type_id` values corresponding
          to each tool integration can be found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :param dict parameters: (optional) Unique key-value pairs representing
          parameters to be used to create the tool. A list of parameters for each tool
          integration can be found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        tool_type_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> None:
        """
        Initialize a ToolchainToolPrototypePatch object.

        :param str name: (optional) Name of the tool.
        :param str tool_type_id: (optional) The unique short name of the tool that
               should be provisioned or updated. A table of `tool_type_id` values
               corresponding to each tool integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param dict parameters: (optional) Unique key-value pairs representing
               parameters to be used to create the tool. A list of parameters for each
               tool integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        """
        self.name = name
        self.tool_type_id = tool_type_id
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolPrototypePatch':
        """Initialize a ToolchainToolPrototypePatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (tool_type_id := _dict.get('tool_type_id')) is not None:
            args['tool_type_id'] = tool_type_id
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = parameters
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolPrototypePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolPrototypePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolPrototypePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolPrototypePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


##############################################################################
# Pagers
##############################################################################


class ToolchainsPager:
    """
    ToolchainsPager can be used to simplify the use of the "list_toolchains" method.
    """

    def __init__(
        self,
        *,
        client: CdToolchainV2,
        resource_group_id: str,
        limit: int = None,
        name: str = None,
    ) -> None:
        """
        Initialize a ToolchainsPager object.
        :param str resource_group_id: The resource group ID where the toolchains
               exist.
        :param int limit: (optional) Limit the number of results.
        :param str name: (optional) Exact name of toolchain to look up. This
               parameter is case sensitive.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._resource_group_id = resource_group_id
        self._limit = limit
        self._name = name

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ToolchainModel.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_toolchains(
            resource_group_id=self._resource_group_id,
            limit=self._limit,
            name=self._name,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('toolchains')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ToolchainModel.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ToolsPager:
    """
    ToolsPager can be used to simplify the use of the "list_tools" method.
    """

    def __init__(
        self,
        *,
        client: CdToolchainV2,
        toolchain_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a ToolsPager object.
        :param str toolchain_id: ID of the toolchain that tools are bound to.
        :param int limit: (optional) Limit the number of results.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._toolchain_id = toolchain_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ToolModel.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_tools(
            toolchain_id=self._toolchain_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('tools')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ToolModel.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results

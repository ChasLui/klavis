import logging
from typing import Any, Dict, Optional, List
from .base import make_v2_request

# Configure logging
logger = logging.getLogger(__name__)

async def get_all_persons(
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    ids: Optional[List[int]] = None,
    field_ids: Optional[List[str]] = None,
    field_types: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Get all Persons in Affinity.
    
    Args:
        cursor: Cursor for pagination
        limit: Number of items per page (1-100, default 100)
        ids: Person IDs to filter by
        field_ids: Field IDs for field data
        field_types: Field types (enriched, global, relationship-intelligence)
    """
    logger.info("Executing tool: get_all_persons")
    try:
        params = {}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        if ids:
            params["ids"] = ids
        if field_ids:
            params["fieldIds"] = field_ids
        if field_types:
            params["fieldTypes"] = field_types
            
        return await make_v2_request("GET", "/persons", params=params)
    except Exception as e:
        logger.exception(f"Error executing tool get_all_persons: {e}")
        raise e

async def get_single_person(
    person_id: int,
    field_ids: Optional[List[str]] = None,
    field_types: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Get a single Person by ID.
    
    Args:
        person_id: Person ID
        field_ids: Field IDs for field data
        field_types: Field types (enriched, global, relationship-intelligence)
    """
    logger.info(f"Executing tool: get_single_person with person_id: {person_id}")
    try:
        params = {}
        if field_ids:
            params["fieldIds"] = field_ids
        if field_types:
            params["fieldTypes"] = field_types
            
        return await make_v2_request("GET", f"/persons/{person_id}", params=params)
    except Exception as e:
        logger.exception(f"Error executing tool get_single_person: {e}")
        raise e

async def get_person_fields_metadata(
    cursor: Optional[str] = None,
    limit: Optional[int] = None
) -> Dict[str, Any]:
    """Get metadata on Person Fields.
    
    Args:
        cursor: Cursor for pagination
        limit: Number of items per page (1-100, default 100)
    """
    logger.info("Executing tool: get_person_fields_metadata")
    try:
        params = {}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
            
        return await make_v2_request("GET", "/persons/fields", params=params)
    except Exception as e:
        logger.exception(f"Error executing tool get_person_fields_metadata: {e}")
        raise e

async def get_person_lists(
    person_id: int,
    cursor: Optional[str] = None,
    limit: Optional[int] = None
) -> Dict[str, Any]:
    """Get a Person's Lists.
    
    Args:
        person_id: Person ID
        cursor: Cursor for pagination
        limit: Number of items per page (1-100, default 100)
    """
    logger.info(f"Executing tool: get_person_lists with person_id: {person_id}")
    try:
        params = {}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
            
        return await make_v2_request("GET", f"/persons/{person_id}/lists", params=params)
    except Exception as e:
        logger.exception(f"Error executing tool get_person_lists: {e}")
        raise e

async def get_person_list_entries(
    person_id: int,
    cursor: Optional[str] = None,
    limit: Optional[int] = None
) -> Dict[str, Any]:
    """Get a Person's List Entries.
    
    Args:
        person_id: Person ID
        cursor: Cursor for pagination
        limit: Number of items per page (1-100, default 100)
    """
    logger.info(f"Executing tool: get_person_list_entries with person_id: {person_id}")
    try:
        params = {}
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
            
        return await make_v2_request("GET", f"/persons/{person_id}/list-entries", params=params)
    except Exception as e:
        logger.exception(f"Error executing tool get_person_list_entries: {e}")
        raise e 
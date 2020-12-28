/* tslint:disable */
/* eslint-disable */
/**
 * Civ VI City Planner
 * Optomize your civ vi city plans
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    CityTiles,
    CityTilesFromJSON,
    CityTilesFromJSONTyped,
    CityTilesToJSON,
} from './';

/**
 * 
 * @export
 * @interface City
 */
export interface City {
    /**
     * 
     * @type {string}
     * @memberof City
     */
    name?: string;
    /**
     * 
     * @type {CityTiles}
     * @memberof City
     */
    tiles?: CityTiles;
}

export function CityFromJSON(json: any): City {
    return CityFromJSONTyped(json, false);
}

export function CityFromJSONTyped(json: any, ignoreDiscriminator: boolean): City {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'tiles': !exists(json, 'tiles') ? undefined : CityTilesFromJSON(json['tiles']),
    };
}

export function CityToJSON(value?: City | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'tiles': CityTilesToJSON(value.tiles),
    };
}


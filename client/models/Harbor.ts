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
    District,
    DistrictFromJSON,
    DistrictFromJSONTyped,
    DistrictToJSON,
    HarborAllOf,
    HarborAllOfFromJSON,
    HarborAllOfFromJSONTyped,
    HarborAllOfToJSON,
} from './';

/**
 * 
 * @export
 * @interface Harbor
 */
export interface Harbor extends District {
    /**
     * 
     * @type {Array<string>}
     * @memberof Harbor
     */
    buildings?: Array<HarborBuildingsEnum>;
}

export function HarborFromJSON(json: any): Harbor {
    return HarborFromJSONTyped(json, false);
}

export function HarborFromJSONTyped(json: any, ignoreDiscriminator: boolean): Harbor {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        ...DistrictFromJSONTyped(json, ignoreDiscriminator),
        'buildings': !exists(json, 'buildings') ? undefined : json['buildings'],
    };
}

export function HarborToJSON(value?: Harbor | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        ...DistrictToJSON(value),
        'buildings': value.buildings,
    };
}

/**
* @export
* @enum {string}
*/
export enum HarborBuildingsEnum {
    Lighthouse = 'lighthouse',
    Shipyard = 'shipyard',
    Seaport = 'seaport'
}


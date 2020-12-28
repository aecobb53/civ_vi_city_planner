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
    CampusAllOf,
    CampusAllOfFromJSON,
    CampusAllOfFromJSONTyped,
    CampusAllOfToJSON,
    District,
    DistrictFromJSON,
    DistrictFromJSONTyped,
    DistrictToJSON,
} from './';

/**
 * 
 * @export
 * @interface Campus
 */
export interface Campus extends District {
    /**
     * 
     * @type {Array<string>}
     * @memberof Campus
     */
    buildings?: Array<CampusBuildingsEnum>;
}

export function CampusFromJSON(json: any): Campus {
    return CampusFromJSONTyped(json, false);
}

export function CampusFromJSONTyped(json: any, ignoreDiscriminator: boolean): Campus {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        ...DistrictFromJSONTyped(json, ignoreDiscriminator),
        'buildings': !exists(json, 'buildings') ? undefined : json['buildings'],
    };
}

export function CampusToJSON(value?: Campus | null): any {
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
export enum CampusBuildingsEnum {
    Library = 'library',
    University = 'university',
    ResearchLab = 'research_lab'
}


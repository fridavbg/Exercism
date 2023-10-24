// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Removes duplicate tracks from a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} new playlist with unique entries
 */
export function removeDuplicates(playlist) {
    let noDuplicates = [...new Set(playlist)];
    return noDuplicates;
}

/**
 * Checks whether a playlist includes a track.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {boolean} whether the track is in the playlist
 */
export function hasTrack(playlist, track) {
    return playlist.includes(track);
}

/**
 * Adds a track to a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function addTrack(playlist, track) {
    if (!hasTrack(playlist, track)) {
        playlist.push(track);
    }
    return playlist;
}
//

/**
 * Deletes a track from a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function deleteTrack(playlist, track) {
    let index = playlist.indexOf(track);
    if (index >= 0) {
        playlist.splice(index, 1);
    }
    return playlist;
}

/**
 * Lists the unique artists in a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} list of artists
 */
export function listArtists(playlist) {
    let artists = new Set();
    for (let i = 0; i < playlist.length; i++) {
        const element = playlist[i];
        let artistIndex = element.indexOf("-") + 2;
        artists.add(element.slice(artistIndex, element.length));
    }
    return [...artists];
}

const playlist = [
    "All Mine - Portishead",
    "Sight to Behold - Devendra Banhart",
    "Sour Times - Portishead",
];

console.log(listArtists(playlist));

import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";

import type { CompanyInfo, UpdateOrCreateMemoRequestBody } from "../../types";
import Api from "../../utils/api";

interface MemoState {
    sidCompanyInfoMap: { [sid: string]: CompanyInfo };
    favorites: string[];
    isWaiting: boolean;
}

const initialState: MemoState = {
    sidCompanyInfoMap: {},
    favorites: [],
    isWaiting: false,
};

export const fetchCompanyInfo = createAsyncThunk(
    "memo/fetchCompanyInfo",
    async (sid: string): Promise<CompanyInfo | undefined> => {
        const response = await Api.sendRequest(
            `memo/company-info?sids=${sid}`,
            "get"
        );
        if (response?.success) return response.data[0];
        else throw Error("Failed to fetch company info.");
    }
);

export const updateOrCreateMemo = createAsyncThunk(
    "memo/updateOrCreateMemo",
    async (
        requestBody: UpdateOrCreateMemoRequestBody
    ): Promise<CompanyInfo> => {
        const response = await Api.sendRequest(
            `memo/stock-memo/${requestBody.sid}`,
            "post",
            JSON.stringify(requestBody)
        );
        navigator.vibrate(20);
        if (response?.success) return response.data;
        else throw Error("Failed to update/create memo.");
    }
);

export const fetchAllFavorites = createAsyncThunk(
    "memo/fetchAllFavorites",
    async (): Promise<string[]> => {
        const response = await Api.sendRequest("memo/favorites", "get");
        if (response?.success) return response.data;
        else throw Error("Failed to fetch favorites.");
    }
);

export const addToFavorites = createAsyncThunk(
    "memo/addToFavorite",
    async (sid: string): Promise<string> => {
        const response = await Api.sendRequest(
            `memo/favorite/${sid}`,
            "post",
            JSON.stringify({})
        );
        if (response?.success) return response.data;
        else throw Error("Failed to add to favorites.");
    }
);

export const removeFromFavorites = createAsyncThunk(
    "memo/removeFromFavorites",
    async (sid: string): Promise<string> => {
        const response = await Api.sendRequest(
            `memo/favorite/${sid}`,
            "delete"
        );
        if (response?.success) return response.data;
        else throw Error("Failed to remove from favorites.");
    }
);

export const memoSlice = createSlice({
    name: "memo",
    initialState,
    reducers: {
        refreshAllCompanyInfoWithNonCacheResponse(
            state,
            action: PayloadAction<CompanyInfo[]>
        ) {
            for (const i of action.payload) state.sidCompanyInfoMap[i.sid] = i;
        },
        refreshFavoritesWithNonCacheResponse(
            state,
            action: PayloadAction<string[]>
        ) {
            state.favorites = [...action.payload];
        },
        fakeAddToFavorites(state, action: PayloadAction<string>) {
            const sid = action.payload;
            if (!state.favorites.includes(sid)) state.favorites.push(sid);
        },
        fakeRemoveFromFavorites(state, action: PayloadAction<string>) {
            const sidToRemove = action.payload;
            const idx = state.favorites.findIndex((sid) => sid === sidToRemove);
            if (idx !== -1) state.favorites.splice(idx, 1);
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchCompanyInfo.pending, (state) => {
                state.isWaiting = true;
            })
            .addCase(fetchCompanyInfo.fulfilled, (state, action) => {
                const companyInfo = action.payload;
                if (companyInfo !== undefined) {
                    state.sidCompanyInfoMap[companyInfo.sid] = companyInfo;
                }
                state.isWaiting = false;
            })
            .addCase(fetchCompanyInfo.rejected, (state) => {
                state.isWaiting = false;
            })

            .addCase(updateOrCreateMemo.pending, (state) => {
                state.isWaiting = true;
            })
            .addCase(updateOrCreateMemo.fulfilled, (state, action) => {
                state.sidCompanyInfoMap[action.payload.sid] = action.payload;
                state.isWaiting = false;
            })
            .addCase(updateOrCreateMemo.rejected, (state) => {
                state.isWaiting = false;
            })

            .addCase(fetchAllFavorites.pending, (state) => {
                state.isWaiting = true;
            })
            .addCase(fetchAllFavorites.fulfilled, (state, action) => {
                state.favorites = [...action.payload];
                state.isWaiting = false;
            })
            .addCase(fetchAllFavorites.rejected, (state) => {
                state.isWaiting = false;
            })

            .addCase(addToFavorites.pending, (state) => {
                state.isWaiting = true;
            })
            .addCase(addToFavorites.fulfilled, (state, action) => {
                const sid = action.payload;
                if (!state.favorites.includes(sid)) state.favorites.push(sid);
                state.isWaiting = false;
            })
            .addCase(addToFavorites.rejected, (state) => {
                state.isWaiting = false;
            })

            .addCase(removeFromFavorites.pending, (state) => {
                state.isWaiting = true;
            })
            .addCase(removeFromFavorites.fulfilled, (state, action) => {
                const sidToRemove = action.payload;
                const idx = state.favorites.findIndex(
                    (sid) => sid === sidToRemove
                );
                if (idx !== -1) state.favorites.splice(idx, 1);
                state.isWaiting = false;
            })
            .addCase(removeFromFavorites.rejected, (state) => {
                state.isWaiting = false;
            });
    },
});

export const {
    refreshAllCompanyInfoWithNonCacheResponse,
    refreshFavoritesWithNonCacheResponse,
    fakeAddToFavorites,
    fakeRemoveFromFavorites,
} = memoSlice.actions;
export default memoSlice.reducer;

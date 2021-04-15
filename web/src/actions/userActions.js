import {
  USER_LOGIN_FAIL,
  USER_LOGIN_REQUEST,
  USER_LOGIN_SUCCESS,
  USER_LOGOUT_REQUEST,
  USER_REGISTER_REQUEST,
  USER_REGISTER_FAIL,
  USER_REGISTER_SUCCESS,
  USER_DETAILS_REQUEST,
  USER_DETAILS_SUCCESS,
  USER_DETAILS_FAIL,
  USER_UPDATE_PROFILE_FAIL,
  USER_UPDATE_PROFILE_SUCCESS,
  USER_UPDATE_PROFILE_REQUEST,
  USER_UPDATE_PROFILE_RESET,
  USER_GROUP_FAIL,
  USER_GROUP_SUCCESS,
  USER_GROUP_REQUEST,
  USER_LIST_REQUEST,
  USER_LIST_SUCCESS,
  USER_LIST_FAIL,
} from "../constants/userConstants";
import axios from "axios";
export const login = (username, password) => async (dispatch) => {
  try {
    dispatch({
      type: USER_LOGIN_REQUEST,
    });
    let config = {
      headers: {
        "Content-Type": "Application/json",
      },
    };

    const response = await axios.post(
      "/auth/token/login/",
      { username, password },
      config
    );
    let auth_token = response.data.auth_token;
    config = {
      headers: {
        "Content-Type": "Application/json",
        Authorization: `Token ${auth_token}`,
      },
    };

    const { data } = await axios.get(`/api/users/me`, config);
    const payload = { auth_token, ...data };
    console.log(payload);
    console.log(data);
    localStorage.setItem("userInfo", JSON.stringify(payload));
    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: payload,
    });
  } catch (error) {
    dispatch({
      type: USER_LOGIN_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const logout = () => async (dispatch) => {
  localStorage.removeItem("userInfo");
  dispatch({
    type: USER_LOGOUT_REQUEST,
  });
};

export const register = (username, email, password) => async (dispatch) => {
  try {
    dispatch({
      type: USER_REGISTER_REQUEST,
    });
    const config = {
      headers: {
        "Content-Type": "Application/json",
      },
    };

    const { data } = await axios.post(
      "/auth/users/",
      { username, email, password },
      config
    );
    dispatch({
      type: USER_REGISTER_SUCCESS,
      payload: data,
    });

    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: USER_REGISTER_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const getUserDetail = (id) => async (dispatch, getState) => {
  try {
    dispatch({
      type: USER_DETAILS_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-Type": "Application/json",
        Authorization: `Token ${userInfo.auth_token}`,
      },
    };

    const { data } = await axios.get(`/api/users/${id}`, config);
    localStorage.setItem("userInfo", JSON.stringify({ ...data, ...userInfo }));
    dispatch({
      type: USER_DETAILS_SUCCESS,
      payload: { ...data, ...userInfo },
    });
  } catch (error) {
    dispatch({
      type: USER_DETAILS_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const getUsers = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: USER_LIST_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-Type": "Application/json",
        Authorization: `Token ${userInfo.auth_token}`,
      },
    };
    const { data } = await axios.get(`/api/users/`, config);
    dispatch({
      type: USER_LIST_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: USER_LIST_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const setUserGroup = (user, group) => async (dispatch,getState) => {
  try {
    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-Type": "Application/json",
        Authorization: `Token ${userInfo.auth_token}`,
      },
    };
    const { data } = await axios.post(
      `/api/users/${user.username}/groups/`,
      { group },
      config
    );
    return { user, group };
  } catch (error) {
    throw error
  }
};

export const updateUserProfile = (user) => async (dispatch, getState) => {
  try {
    dispatch({
      type: USER_UPDATE_PROFILE_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-Type": "Application/json",
        Authorization: `Token ${userInfo.token}`,
      },
    };
    console.log("Axios PUT request");
    const { data } = await axios.put(`/api/users/me`, user, config);

    dispatch({
      type: USER_UPDATE_PROFILE_SUCCESS,
      payload: data,
    });
    localStorage.setItem("userInfo", JSON.stringify(data));
    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: USER_UPDATE_PROFILE_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const resetUserProfileState = () => async (dispatch) => {
  dispatch({
    type: USER_UPDATE_PROFILE_RESET,
  });
};

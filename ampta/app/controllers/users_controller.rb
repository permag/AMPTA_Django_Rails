class UsersController < ApplicationController
  before_filter :confirm_logged_in, :except => [:new, :create]
  before_filter :sidenav
  
  def index
    @users = User.all
  end

  def show
    @user = User.find(params[:id])
  end

  def new
    @user = User.new
    render :layout => 'login_page'
  end

  def create
    @user = User.new(params[:user])
    respond_to do |format|
      if @user.save
        format.html { redirect_to login_path, :notice => "Thank you for registering. Please login." }
      else
        format.html { render :action => "new", :layout => 'login_page' }
      end
    end
  end

end
